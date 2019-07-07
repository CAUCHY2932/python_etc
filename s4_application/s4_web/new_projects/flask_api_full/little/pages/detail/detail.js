import { HTTP } from '../../utils/http.js'

var http = new HTTP()

Page({
  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var isbn = options.isbn
    console.log(isbn) // '9787111128069'
    this.setData({
      isbn: isbn
    })
  }
})