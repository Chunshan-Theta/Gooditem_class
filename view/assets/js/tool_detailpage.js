
let urlParams = new URLSearchParams(window.location.search);
var comment_id = urlParams.get('comment_id'); // true
rest_get_id_comment(comment_id, function(data){
    console.log(data);
    $("#main_title").html(data['class_name']+" "+data['teacher_name']);
    $("#left-side").html(data['major']+"<br>"+data['cost']+"<br>"+data['value']);
    var homework = (data['homework'] == '1')? "“會”有回家作業" : "“不會”有回家作業";
    var classexam = (data['homework'] == '1')? "課堂中“會”有考試" : "課堂中“不會”有考試";
    var classcall = (data['homework'] == '1')? "課堂中“會”有點名" : "課堂中“不會”有點名";
    $("#right-side").html("期中考："+data['midexam']+"<br>期末考："+data['endexam']+"<br>"+classcall+"<br>"+classexam+"<br>"+homework);
    $("#main_comment").html(data['user_memo']);

});

rest_get_id_replay(comment_id, function(data){
    console.log(data);
    var idx =data.length+1;
    data.forEach(function(content){
        idx -=1;
	    var object1 = "<div><div>"+idx+"f\t</div>"+content["user_memo"]+"</div>";
        $("#main_reply").append(object1);
    });

});
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
$("#send_comment_button").click(function(){
    var user_memo = $("#user_memo").val();
    var body = {
      "comment_id": Number(comment_id),
      "object_type": "normal",
      "replay_id": 1,
      "request_status": "success",
      "user_memo": user_memo
    }
    rest_post_reply(body,function(result){
        console.log(result)
        if(result == "ok"){
            window.location.reload();
        }else{
            alert("error");
        }
    });
});