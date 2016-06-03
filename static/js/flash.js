// JavaScript Document

$(document).ready(function(){
			$("#lione").mouseover(function(){
			 $("#lione").removeClass("one");
			    $("#lione").addClass("onesel");
			});
			 $("#lione").mouseout(function(){
			 
			    $("#lione").addClass("one");
			    $("#lione").removeClass("onesel");
			});
			
		   var ullist = $('ul.fast_guidul li');
			ullist.each(function(index) {
				var cc = $(this);
				
				$("ul.fast_guidul li:even").css("background","#f1f1f1");
				
				});
			$("#nav_zhankai").mouseover(function(){
			 
			   $(".xs_dh").hide("");
			   $(".yc_dh").show("");
			});
			
			$("#nav_zhankai").mouseout(function(){
			 $(".xs_dh").hide("");
			 $(".yc_dh").hide("");
			  
			});
			
			$("#nav_shouqi").mouseover(function(){
			 
			   $(".xs_dh").show("");
			   $(".yc_dh").hide("");
			});
			
			$("#nav_shouqi").mouseout(function(){
			 $(".xs_dh").hide("");
			 $(".yc_dh").hide("");
			  
			});
});
/*topnav*/
 function look_title(){
    var text1=$('#looknews').html();
	var text='只看标题';
	var planItems = $('ul.news_list_ul li');
	
	
	
		planItems.each(function(index) {
			var li = $(this);
			var news_xgxw = li.find('div.news_xgxw');
			var news_content=li.find('div.news_content');
		    var news_xgxw_con=li.find('div.news_xgxw_con');
		    var moren_right=li.find('div.moren_list div.moren_right');
			var moren_rightimg=li.find('div.moren_list div.moren_right img');
			var tupian_conul=li.find('div.tupian_conul')	
			
	
			
			
			
		if(text1 == text){
		
			
		$('#looknews').html('查看图片');
		
				news_xgxw.hide();
			    news_content.hide();
				news_xgxw_con.hide();
				tupian_conul.hide();
				moren_right.css('margin-top','0px');
				moren_right.css('width','90px');
				moren_right.css('height','70px');
				
				moren_rightimg.css('width','90px');
				moren_rightimg.css('height','70px');
				
		}else{
			
	
		$('#looknews').html('只看标题');
		      news_xgxw.show();
				news_content.show();
				tupian_conul.show();
				moren_right.css('margin-top','36px');
				moren_right.css('width','130px');
				moren_right.css('height','95px');
				
				moren_rightimg.css('width','130px');
				moren_rightimg.css('height','95px');
		}
	}
	
	
	
	);
		var top=$(document).scrollTop();
	    var index_topa=$("#index_topa").height();
	    var gg=$("#news_top_advert").height();
		
		 var scrollback=index_topa+gg+45;
		 
		 if(top>=473){
			$("html,body").animate({scrollTop:473},1);
		 }
}
/*daohang huaguo*/
$(document).ready(function(){
function topnav2(){
	  var planItems = $('ul.nav_navcon li');
		planItems.each(function(index) {
		var li = $(this);
		var div= $('li.sel1 a');
			li.mouseover(function() {
				$('ul.nav_navcon li').addClass('');
					li.addClass('sel');
					div.css('border-bottom','none');
				});
			  li.mouseout(function() {
					li.removeClass('sel');
					div.css('border-bottom','5px solid #B21112');
				});
			});
	  };
	  topnav2();
	  function topnav1(){
	var _show = null;
	  var _hideTimer = null;
	  var planItems = $('ul.c-fl-ul li.division');
		planItems.each(function(index) {
	    var li = $(this);
		var div = li.find('div.navshow_div');
			div.css("display","none");
			li.bind('mouseenter',function() {
				if (_show != null) {
					clearTimeout(_show);
				}
				_show = setTimeout(function() {
					$('ul.nav_navcon li').addClass('');
					
					li.addClass('topnav_sel');
				}, 20);
				});
			  li.bind('mouseleave', function() {
					if (_show != null) {
					clearTimeout(_show);
				}
				_hideTimer = setTimeout(function() {
					li.removeClass('topnav_sel');
					
				}, 20);
				});
			});
	  };
	topnav1();
	  
});

 //tab
function blog_nTabs(thisObjb,Numb){
if(thisObjb.className == "blog_sel")return;
var thisObjb = thisObjb.parentNode.id;
var tabList = document.getElementById(thisObjb).getElementsByTagName("li");
for(i=0; i <tabList.length; i++)
{
  if (i == Numb)
  {
   tabList[Numb].className = "blog_sel"; 
      document.getElementById(thisObjb+"_Content"+i).style.display = "block";
  }else{
   tabList[i].className = "normal"; 
   document.getElementById(thisObjb+"_Content"+i).style.display = "none";
  }
} 
}
/**/
function didi(id) {
     document.getElementById("id").className="di"+id;
  }
  
function did(id) {
     document.getElementById("id1").className="dii"+id;
  }

function did1(id) {
     document.getElementById("id2").className="dii1"+id;
  }
  function did2(id) {
     document.getElementById("id3").className="dii2"+id;
  }
   function did3(id) {
     document.getElementById("id4").className="dii3"+id;
   }
     function did4(id) {
     document.getElementById("id5").className="dii4"+id;
  }
     function did5(id) {
     document.getElementById("id6").className="dii5"+id;
  }
   function search_select(id) {
     document.getElementById("id7").className="dii7"+id;
  }
     function weibo(id) {
     document.getElementById("id8").className="dii8"+id;
  }
   function search_jsxw(id) {
     document.getElementById("idjsxw").className="diijsxw"+id;
  }
/*small daohang show*/
 function topnav(){
    var text1=$('#nav_zhankai').html();
	var text='';
	if(text1 == text){
		$('#nav_zhankai').html(',');
		$('#nav_zhankai').show();
		$('#nav_shouqi').hide();
		$('.nav_boxcon').css('height','74px');
		$('.nav_boxcon').css('margin-top','5px');
		$('ul.nav_navcon').css('display','block');
		
	}
	else{
		$('#nav_zhankai').html('');
		$('#nav_zhankai').hide();
		$('#nav_shouqi').show();
		$('.nav_boxcon').css('height','2px');
		$('.nav_boxcon').css('margin-top','0px');
		$('ul.nav_navcon').css('display','none');
	}
}
/*lunhuan*/
var times=0;
function focusBox(o,n){
	if(!o) return;
	var w=403, $o=$('#'+o),i=0,l=0;arr= [],t= null,
		$infoLi = $o.find('.banner_info li'), len= $infoLi.length*2,
		$ul=$o.find('.banner_pic>ul');
	$ul.append($ul.html()).css({'width':len*w, 'left': -len*w/2});
	$infoLi.eq(0).addClass('current');
	//add banner_pages element
	arr.push('<div class="banner_pages"><ul>');
	$infoLi.each(function(i){
		if(i==0){
			arr.push('<li class="current"><span>'+ (i+1) +'</span></li>');
		}else{
			arr.push('<li><span>'+ (i+1) +'</span></li>');
		}
	});
	arr.push('</ul></div>');
	$o.append(arr.join(''));
	var $pagesLi = $o.find('.banner_pages li');
	//mouse
	$pagesLi.children('span').click(function(){
		var p = $pagesLi.index($o.find('.banner_pages li.current'));
		i = $pagesLi.children('span').index($(this));
		if(i==p) return;
		l = parseInt($ul.css('left')) + w*(p-i);
		addCurrent(i,l);
		return false;
	})
	$o.children('a.btn_prev').click(function(){
		i = $pagesLi.index($o.find('.banner_pages li.current'));
		(i==0)? i=(len/2-1):i--;
		l = parseInt($ul.css('left')) + w;
		addCurrent(i,l);
		return false;
	})
	$o.children('a.btn_next').click(function(){
		i = ($pagesLi.index($o.find('.banner_pages li.current'))+1)%(len/2);
		l = parseInt($ul.css('left')) - w;
		addCurrent(i,l);
		return false;
	})
	//auto focus
	
	t = setInterval(init,3500);
	
	$o.hover(function(){
		clearInterval(t);
	}, function(){
		t = setInterval(init,3500);
		
	});
	
	function init(){
		if(times < n){
		times++;
		$o.children('a.btn_next').trigger('click');
		}else{
			return ;	
		}
	}
	//add focus
	function addCurrent(i,l){
		if($ul.is(':animated')) return;
		$ul.animate({'left':l},500,function(){
			$o.children('.banner_count').text(i+1);
			$infoLi.not($infoLi.eq(i).addClass('current')).removeClass('current');
			$pagesLi.not($pagesLi.eq(i).addClass('current')).removeClass('current');
			if(l== (1-len)*w){
				$ul.css({'left'
: (1-len/2)*w});
			}else if(l== 0){
				$ul.css({'left': -len*w/2});
			}
		});
	}
}

$(function(){
	focusBox('kakaFocus',10000);
})




/*navlist*/
$(document).ready(function(){
	$("#kakaFocus").mouseover(function(){
		  $("#lrbt_show1").show();
		   $("#lrbt_show2").show();
		});
		$("#kakaFocus").mouseout(function(){
	  	   $("#lrbt_show1").hide();
		   $("#lrbt_show2").hide();
		});
	 
	});
 
 //tab
function nTabs(thisObj,Num){
if(thisObj.className == "active")return;
var tabObj = thisObj.parentNode.id;
var tabList = document.getElementById(tabObj).getElementsByTagName("li");
for(i=0; i <tabList.length; i++)
{
  if (i == Num)
  {
   thisObj.className = "active"; 
      document.getElementById(tabObj+"_Content"+i).style.display = "block";
  }else{
   tabList[i].className = "normal"; 
   document.getElementById(tabObj+"_Content"+i).style.display = "none";
  }
} 
}
/**/
 /*list滑过*/
 $(document).ready(function(){
	 var _show = null;
	  var _hideTimer = null;
	  var planItems = $('.news_list_ulbox ul li');
	  var _tupian_li = $('.news_list_ulbox ul li._tupian_li');
	 planItems.each(function(index) {
	var li = $(this);
		    var news_xgxw = li.find('div.news_xgxw .news_xgxw_a');
			var sharenews=li.find('div.video_con1_title_right');
			var news_xgxw_con=li.find('div.news_xgxw_con');
			var planItems_tp = li.find('div.tupian_conul ul li');
		    planItems_tp.each(function() {
				  var tpli = $(this); 
				  var tp_blackbg = tpli.find('div.tp_blackbg');
				 
				 tpli.bind('mouseenter',function() {
					 tp_blackbg.hide();
				  });
				  
				  tpli.bind('mouseleave',function() {
					  tp_blackbg.show();
				  });
			 });
	news_xgxw_con.hide();
	sharenews.hide('');
	/*topnav*/
	news_xgxw.click(function(){ 
			var text_xgxw0=news_xgxw.html();
			var text_xgxw='相关新闻<img src="http://i6.chinanews.com/2013/news/images/xgimg.jpg">';
			//alert(text_xgxw.toLowerCase());
			if(text_xgxw0.toLowerCase() == text_xgxw.toLowerCase()){
			news_xgxw.html('相关新闻<img src="http://i6.chinanews.com/2013/news/images/xg_upimg.jpg">');
					  news_xgxw_con.show();
					  news_xgxw.removeClass("news_xgxw_al");
					  news_xgxw.addClass("news_xgxw_asel");
					  sharenews.show();
			}else{
			news_xgxw.html('相关新闻<img src="http://i6.chinanews.com/2013/news/images/xgimg.jpg">');
				  news_xgxw_con.hide();
				  news_xgxw.addClass("news_xgxw_al");
				  news_xgxw.removeClass("news_xgxw_asel");
				  sharenews.hide();
			}
		})
		/**/
		li.bind('mouseenter',function() {
				if (_show != null) {
					clearTimeout(_show);
				}
				_show = setTimeout(function() {
					$('ul._commuity_nav li div.conbox').hide();
					li.css('background','#eeeeee');
					$(".module_advert_ul li").css('background','none');
					_tupian_li.css('background','none');
					sharenews.show('');
				/**/
					
				}, 20);
				});
			  li.bind('mouseleave', function() {
					if (_show != null) {
					clearTimeout(_show);
				}
				_hideTimer = setTimeout(function() {
					
					li.css('background','none');
					sharenews.hide('');
					
				/**/
					
				}, 20);
				});
		});
	 
});


/*即时新闻*/
 $(document).ready(function(){
		var planItems = $('ul._tab-list li');
		planItems.each(function(index) {
	   var li = $(this);
			li.click(function(index){
			$('ul._tab-list li').removeClass("filter-selected");
			li.addClass("filter-selected");
			var listatext=li.html();
			$("#jsxw_title_text").html('即时新闻 &gt; '+listatext);
			/**/
		}); 
			
		});
	 
});

 //jsxwtab
function js_jsxwselect(thisObj,Num){
if(thisObj.className == "active")return;

document.getElementById("idjsxw").className="diijsxw1";
var tabObj = thisObj.parentNode.id;
var tabList = document.getElementById(tabObj).getElementsByTagName("li");
for(i=0; i <tabList.length; i++)
{
 if (i == Num)
  {
   tabList[Num].className = "active"; 
      document.getElementById(tabObj+"_Con"+i).style.display = "block";
	  
	  var cc=document.getElementById(tabObj).getElementsByTagName("a")[Num].innerHTML;
	  
	   var top=$(document).scrollTop();
	    var index_topa=$("#index_topa").height();
	    var gg=$("#news_top_advert").height();
		
		 var scrollback=index_topa+gg+45;
		 
		  if(top>=473){
			$("html,body").animate({scrollTop:473},1);
			}
	  $("#jsxw_select").html(cc);
	  //alert(cc);
 			  $("#jsxw_all_Con0").hide();
			  $("#jsxw_all_Con1").hide();
			  $("#jsxw_all_Con2").hide();
			  $("#jsxw_all_Con3").hide();
			  $("#jsxw_all_Con4").hide();
			  $("#jsxw_all_Con5").hide();
			  $("#jsxw_all_Con6").hide();
			  $("#jsxw_all_Con7").hide();
			  $("#jsxw_all_Con8").hide();
			  $("#jsxw_all_Con9").hide();
			  
			  $("#jsxw_sp_Con0").hide();
			  $("#jsxw_sp_Con1").hide();
			  $("#jsxw_sp_Con2").hide();
			  $("#jsxw_sp_Con3").hide();
			  $("#jsxw_sp_Con4").hide();
			  $("#jsxw_sp_Con5").hide();
			  $("#jsxw_sp_Con6").hide();
			  $("#jsxw_sp_Con7").hide();
			  $("#jsxw_sp_Con8").hide();
			  $("#jsxwredbox_biglist2").hide();
			if(cc =="视频新闻"){
		  $('#jsxw_title_text').html("视频新闻 &gt; 全部");
		  $('#jsxwredbox_Con1 ul li').removeClass('filter-selected');
		  $('#jsxwredbox_Con1 ul li:first').addClass('filter-selected');
		  $("#jsxw_sp_Con0").show();
		  $('.jsxw_bright').hide();
		  }
		   else if(cc=="图片新闻"){
			  $('#jsxw_title_text').html("图片新闻");
			  $("#jsxwredbox_biglist2").show();
			   $('.jsxw_bright').show();
			  }
			else if(cc=="即时新闻"){
				 $("#jsxw_all_Con0").show();
			  $('#jsxw_title_text').html("即时新闻 &gt; 全部");  
			  $('#jsxwredbox_Con0 ul li').removeClass('filter-selected');
			  $('#jsxwredbox_Con0 ul li:first').addClass('filter-selected');
			   $('.jsxw_bright').show();
			}
	}else{
   tabList[i].className = "normal"; 
   document.getElementById(tabObj+"_Con"+i).style.display = "none";
  }
} 
}
/**/
function jsxw_conshow(obj){
	
	  var _show = null;
	  var _hideTimer = null;
	
	  var _tupian_li = $('.news_list_ulbox ul li._tupian_li');
		obj.each(function() {
		  var li = $(this);
		  
		  //alert(news_xgxw_con);
		    var news_xgxw = li.find('div.news_xgxw .news_xgxw_a');
			var sharenews=li.find('div.video_con1_title_right');
			var news_xgxw_con=li.find('div.news_xgxw_con');
			var planItems_tp = li.find('div.tupian_conul ul li');
			
			
		    planItems_tp.each(function() {
				  var tpli = $(this); 
				  var tp_blackbg = tpli.find('div.tp_blackbg');
				 
				 tpli.bind('mouseenter',function() {
					 tp_blackbg.hide();
				  });
				  
				  tpli.bind('mouseleave',function() {
					  tp_blackbg.show();
				  });
			 });
	news_xgxw_con.hide();
	sharenews.hide('');
	/*topnav*/
	news_xgxw.click(function(){ 
			var text_xgxw0=news_xgxw.html();
			var text_xgxw='相关新闻<img src="http://i6.chinanews.com/2013/news/images/xgimg.jpg">';
			//alert(text_xgxw.toLowerCase());
			if(text_xgxw0.toLowerCase() == text_xgxw.toLowerCase()){
			news_xgxw.html('相关新闻<img src="http://i6.chinanews.com/2013/news/images/xg_upimg.jpg">');
					  news_xgxw_con.show();
					  news_xgxw.removeClass("news_xgxw_al");
					  news_xgxw.addClass("news_xgxw_asel");
					  sharenews.show();
			}else{
			news_xgxw.html('相关新闻<img src="http://i6.chinanews.com/2013/news/images/xgimg.jpg">');
				  news_xgxw_con.hide();
				  news_xgxw.addClass("news_xgxw_al");
				  news_xgxw.removeClass("news_xgxw_asel");
				  sharenews.hide();
			}
		})
		/**/
		
		
		
		
		
		
		
		li.bind('mouseenter',function() {
				if (_show != null) {
					clearTimeout(_show);
				}
				_show = setTimeout(function() {
					$('ul._commuity_nav li div.conbox').hide();
					li.css('background','#eeeeee');
					//alert(00);
					$(".module_advert_ul li").css('background','none');
					_tupian_li.css('background','none');
					sharenews.show('');
				/**/
					
				}, 20);
				});
			  li.bind('mouseleave', function() {
					if (_show != null) {
					clearTimeout(_show);
				}
				_hideTimer = setTimeout(function() {
					
					li.css('background','none');
					sharenews.hide('');
					
				/**/
					
				}, 20);
				});
		    
	   });
			   
	};
	
