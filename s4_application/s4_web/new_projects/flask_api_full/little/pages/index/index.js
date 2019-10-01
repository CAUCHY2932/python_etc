
// import rxwx, { Rx } from '../../utils/RxWX.js'

Page({

  /**
   * 页面的初始数据
   */
  // searchEv: new Rx.Subject(),
  data: {
    inputShowed: false,
    inputVal: "",
    searchKey: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },

  onSearch:function(event){
    var q = event.currentTarget.dataset.text || event.detail.value;
    wx.navigateTo({
      url:'../search/search?q=' + q
    })
  },

  // 显示搜索框
  showInput: function () {
    this.setData({
      inputShowed: true
    });
  },

  // 隐藏搜索框
  hideInput: function () {
    this.setData({
      inputVal: "",
      inputShowed: false
    });
  },

  // 清空搜索框vlaue
  clearInput: function () {
    this.setData({
      inputVal: ""
    });
  },

  // 搜索框的input事件
  inputTyping: function (e) {
    this.setData({
      inputVal: e.detail.value
    });
    // this.searchEv.next(e.detail.value);
  }

})