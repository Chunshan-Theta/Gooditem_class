
function add_block(title, sub_title, content,id,div_name,Detail_page){
	//console.log(title);
	//console.log(sub_title);
	//console.log(content);
	//var id_label = (id%12+1).toString()
	var images_id= "0";
	if(sub_title.search("評價普通") != -1){
	    images_id ="3";
	}
	if(sub_title.search("課程內容充實推薦") != -1){
	    images_id ="1";
	}
	if(sub_title.search("超好過推薦") != -1){
	    images_id ="2";
	}
	if(sub_title.search("毫無收穫") != -1){
	    images_id ="4";
	}
	if(sub_title.search("很容易被當") != -1){
	    images_id ="5";
	}
	var object1 = '<article class="thumb"><a href="images/fulls/'+images_id+'.jpg" class="image"><img src="images/thumbs/'+images_id+'.jpg" alt="" /></a><h1>'+title+'</h1><h2>'+sub_title+'</h2><p>'+content+'<br>'+Detail_page+'</p></article>';
	
	// Merge object2 into object1
	$("#"+div_name).append(object1);
	$("#img_"+images_id).css('background-image', 'url(' +'images/thumbs/'+images_id+'.jpg)');
}

function NextPage(page_num,datas){

	var New_page_block_id = "main_page"+page_num.toString();
	$("#homepage").append("<div class=\"page_num\"><p>Page <"+page_num+"> </p></div>");
	$("#homepage").append("<div id=\""+New_page_block_id+"\" style=\"\" class=\"main_css\"><div>");


	/*
	var num_in_one_page =5;
	for (var i=0; i<=num_in_one_page; i++)
	{ 
	    add_block("程式設計","資訊管理系","123213123123123",i,New_page_block_id);
	}*/
	var temp_count = 0
	datas.forEach(function(item){
	        temp_count+=1;
	        var title = item['class_name']+"<br>"+item['teacher_name'];
	        var sub_title = item['major']+"<br>"+item['cost']+"<br>"+item['value'];
	        var classexam = (item['classexam'] == '1')? "有" : "無";
	        var classcall = (item['classcall'] == '1')? "有" : "無";
	        var homework = (item['homework'] == '1')? "有" : "無";
	        var content= "期中考："+item['midexam']+"<br>期末考："+item['endexam']+"<br>課堂中考試："+classexam+"<br>課堂中點名："+classcall+"<br>回家作業："+homework+"<br>個人簡評："+item['user_memo'];
	        var Detail_page = "<a href=\"Detail.html?comment_id="+item['comment_id']+"\" style=\"cursor: pointer;\">觀看路人留言</a>";
            add_block(title,sub_title,content,temp_count,New_page_block_id,Detail_page);
    });

	var $main = $("#"+New_page_block_id);
	var $body = $('body');
	$main.poptrox({
		baseZIndex: 20000,
		caption: function($a) {

			var s = '';
			//console.log($a)
			$a.nextAll().each(function() {
				s += this.outerHTML;
			});

			return s;

		},
		fadeSpeed: 300,
		onPopupClose: function() { $body.removeClass('modal-active'); },
		onPopupOpen: function() { $body.addClass('modal-active'); },
		overlayOpacity: 0,
		popupCloserText: '',
		popupHeight: 150,
		popupLoaderText: '',
		popupSpeed: 300,
		popupWidth: 150,
		selector: '.thumb > a.image',
		usePopupCaption: true,
		usePopupCloser: true,
		usePopupDefaultStyling: false,
		usePopupForceClose: true,
		usePopupLoader: true,
		usePopupNav: true,
		windowMargin: 50
	});

}

function add_mulit_page(page_num,data){
    var comments = data;
    //console.log(comments);

    NextPage(page_num,comments);
}


