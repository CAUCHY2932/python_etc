// pages/search/search.js
import {HTTP} from '../../utils/http.js'
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
    var q = options.q
    // var q = 'c'
    this.search(q)
  },

  search:function(q){
    var that = this
    var params = {
      url: 'book/search',
      data: {q:q},
      sCallback: function (data) {
        that.setData({
          books:data,
          q:q,
          totalCount:data.length
        })
      },
      eCallback: function () {

      }
    }
    http.request(params)
  }
})