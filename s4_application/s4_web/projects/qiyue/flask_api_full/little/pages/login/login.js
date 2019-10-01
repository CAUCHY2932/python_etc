// pages/login/login.js
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
  
  },

  onSubmit:function(event){
    console.log(event)
    var params = {
      url : 'token',
      data: {
        account: event.detail.value.email,
        secret: event.detail.value.password,
        type: 100
      },
      type:'POST',
      sCallback: function(data){
        wx.setStorageSync('token', data.token)
        wx.showToast({
          title: '成功',
          icon: 'success',
          duration: 2000
        })
        wx.switchTab({
          url:'../index/index'
        })
      },
      eCallback:function(e){
        wx.showToast({
          title: '失败',
          icon: 'cancel',
          duration: 2000
        }) 
      }
    }
    http.request(params)
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})