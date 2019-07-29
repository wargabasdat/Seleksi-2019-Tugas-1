package com.datarequest;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import javax.net.ssl.HttpsURLConnection;
import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.Scanner;

public class HttpRequest {
    private static final Scanner input = new Scanner(System.in);
    private final String USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64); Jesslyn Nathania/13517053@std.stei.itb.ac.id";
    private String address;

    public static void main(String... args) {
        HttpRequest httpRequest = new HttpRequest();
        if (args.length < 1) {
            System.out.print("Input address : ");
            httpRequest.address = input.nextLine();
        }else{
            httpRequest.address = args[0];
        }

        try{
            System.out.println("Testing 1 - Send Http GET request");
            httpRequest.sendGet();
        }catch(Exception e){
            e.printStackTrace();
        }

    }

    // HTTP GET request
    private void sendGet() throws Exception {

        URL url = new URL(this.address);
        HttpsURLConnection con = (HttpsURLConnection) url.openConnection();

        con.setRequestMethod("GET");
        // con.setRequestProperty("Authorization","Bearer "+token);
        con.setRequestProperty("Content-Type", "application/json; charset=UTF-8");

        // add request header
        con.setRequestProperty("User-Agent", USER_AGENT);

        int responseCode = con.getResponseCode();
        System.out.println("\nSending 'GET' request to URL : " + this.address);
        System.out.println("Response Code : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        String htmlString = response.toString();
        Document doc = Jsoup.parse(htmlString);
        Elements tables = doc.getElementsByClass("article__list");
        System.out.println("Table size : "+tables.size());

        for (Element table : tables){
            try {
                String title = table.getElementsByClass("article__list__title")
                        .first()
                        .text();

                String imgHref = table.getElementsByClass("article__list__asset")
                        .first()
                        .select("a")
                        .attr("href");

                String imgSrc = table.select("img")
                        .attr("src");

                String dateInfo = table.getElementsByClass("article__date")
                        .first()
                        .text();

                String category = table.getElementsByClass("article__subtitle")
                        .first()
                        .text();

                if (title!=null && imgHref!=null && imgSrc!=null && dateInfo!=null && category!=null){
                    Data.add(new Data(title,dateInfo,category,imgHref,imgSrc));
                }

            }catch (Exception e){}

        }

        ObjectMapper mapper = new ObjectMapper();

        mapper.writerWithDefaultPrettyPrinter().writeValue(new File("./data/dataJson.json"), Data.getList());

    }
}
