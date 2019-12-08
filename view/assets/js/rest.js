function rest_get_news_comment(start_num,page_num,callback){
    $.get( "https://goodclass.cf:8080/search/0100/comment/newest?start_num="+start_num, function( data ) {
        console.log(data);
        //console.log(callback);
        callback(page_num,data);
    });
}

function rest_get_keywords_comment(keywords,page_num,callback){
    // https://goodclass.cf:8080/search/0100/comment/keyword?keyword=%E8%B3%87%E8%A8%8A
    console.log("https://goodclass.cf:8080/search/0100/comment/keyword?keyword="+keywords);
    $.get( "https://goodclass.cf:8080/search/0100/comment/keyword?keyword="+keywords, function( data ) {
        console.log(data);
        //console.log(callback);
        callback(page_num,data);
    });
}

/*
{
    "class_name": "奇幻中文課",
    "comment_id": 1,
    "object_type": "normal",
    "request_status": "success",
    "teacher_name": "鍾老師",
    "major": "資訊管理系",
    "user_memo": "都100分",
    "midexam": "都給我上台",
    "endexam": "都給我上台！",
    "value": "還不錯啦",
    "cost": "難到爆炸",
    "classcall": 1,
    "homework": 1,
    "classexam": 1
}
*/
function rest_post_keywords_comment(body,callback){
    // https://goodclass.cf:8080/comment/0100/class
    /*
    var body = {
            "class_name": "奇幻中文課",
            "comment_id": 1,
            "object_type": "normal",
            "request_status": "success",
            "teacher_name": "鍾老師",
            "major": "資訊管理系",
            "user_memo": "都100分",
            "midexam": "都給我上台",
            "endexam": "都給我上台！",
            "value": "還不錯啦",
            "cost": "難到爆炸",
            "classcall": 1,
            "homework": 1,
            "classexam": 1
    };*/
    console.log(body);
    $.ajax({
      type: "POST",
      url: "https://goodclass.cf:8080/comment/0100/class",
      data: JSON.stringify(body),
      success: function(result){
            //console.log(result);
            callback("ok");
      },
      error: function(result){
            //console.log(result);
            callback("error");
      },
      contentType: 'application/json',
      dataType: "json"
    });
}
function rest_post_reply(body,callback){
    /*

    https://goodclass.cf:8080/reply/0100/reply

    {
      "comment_id": 52,
      "object_type": "normal",
      "replay_id": 1,
      "request_status": "success",
      "user_memo": "超過100分！"
    }
    */

    console.log(body);
    $.ajax({
      type: "POST",
      url: "https://goodclass.cf:8080/reply/0100/reply",
      data: JSON.stringify(body),
      success: function(result){
            //console.log(result);
            callback("ok");
      },
      error: function(result){
            //console.log(result);
            callback("error");
      },
      contentType: 'application/json',
      dataType: "json"
    });
}
function rest_get_id_comment(comment_id,callback){
    // https://goodclass.cf:8080/search/0100/comment/keyword?keyword=%E8%B3%87%E8%A8%8A
    // var comment_id = 52;
    $.get( "https://goodclass.cf:8080/comment/0100/class?comment_id="+comment_id, function( data ) {
        callback(data);
        //console.log(callback);
        //callback(page_num,data);
    });
}

function rest_get_id_replay(comment_id,callback){
    // https://goodclass.cf:8080/search/0100/reply/under_comment?comment_id=52
    // var comment_id = 52;
    $.get( "https://goodclass.cf:8080/search/0100/reply/under_comment?comment_id="+comment_id, function( data ) {
        callback(data);
        //console.log(callback);
        //callback(page_num,data);
    });
}