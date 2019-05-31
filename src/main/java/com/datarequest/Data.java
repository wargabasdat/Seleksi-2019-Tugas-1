package com.datarequest;

import java.util.ArrayList;
import java.util.List;

public class Data {
    private String title;
    private String dateInfo;
    private String category;
    private String imgHref;
    private String imgSrc;
    private static List<Data> list = new ArrayList<Data>();

    public Data(String _title, String _dateInfo, String _category, String _imgHref, String _imgSrc) {
        title = _title;
        dateInfo = _dateInfo;
        category = _category;
        imgHref = _imgHref;
        imgSrc = _imgSrc;
    }

    public static void add(Data _data){
        list.add(_data);
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDateInfo() {
        return dateInfo;
    }

    public void setDateInfo(String dateInfo) {
        this.dateInfo = dateInfo;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getImgHref() {
        return imgHref;
    }

    public void setImgHref(String imgHref) {
        this.imgHref = imgHref;
    }

    public String getImgSrc() {
        return imgSrc;
    }

    public void setImgSrc(String imgSrc) {
        this.imgSrc = imgSrc;
    }

    public static List<Data> getList() {
        return list;
    }

    public static void setList(List<Data> list) {
        Data.list = list;
    }

    @Override
    public String toString() {
        return "Data{" +
                "title='" + title + '\'' +
                ", dateInfo='" + dateInfo + '\'' +
                ", category='" + category + '\'' +
                ", imgHref='" + imgHref + '\'' +
                ", imgSrc='" + imgSrc + '\'' +
                '}';
    }

}
