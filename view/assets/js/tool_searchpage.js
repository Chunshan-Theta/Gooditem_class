
let urlParams = new URLSearchParams(window.location.search);
var keyword = console.log(urlParams.get('keywords')); // true
rest_get_keywords_comment(urlParams.get('keywords'),1, add_mulit_page);



$("#send_comment_button").click(function(){
    var teacher_name = $("#teacher_name").val();
    var major = $("#major").val();
    var class_name = $("#class_name").val();
    var value = $("#value").val();
    var midexam = $("#midexam").val();
    var endexam = $("#finalclass").val();
    var cost = $("#cost").val();
    var classexam = $("#classexam").val();
    var homework = $("#homework").val();
    var classcall = $("#classcall").val();
    var user_memo = $("#user_memo").val();
    if (teacher_name == ""){
        alert("主講者需填上");
    }else if(major == ""){
        alert("單位名稱需填上 例如：虎科資管、資策會等");

    }else if(class_name == ""){
        alert("課程名稱需填上");
    }else if(value == "-1"){
        alert("短評需選擇");

    }else if(midexam == "-1"){
        alert("期中考需選擇");

    }else if(endexam == "-1"){
        alert("期末考需選擇");

    }else if(cost == "-1"){
        alert("課程難度需選擇");
    }else if(classexam == "-1"){
        alert("課中考試需選擇");

    }else if(homework == "-1"){
        alert("回家作業需選擇");

    }else if(classcall == "-1"){
        alert("固定點名需選擇");

    }
    else{
        var body = {
            "teacher_name":teacher_name,
            "major":major,
            "class_name":class_name,
            "value":value,
            "midexam":midexam,
            "endexam":endexam,
            "cost":cost,
            "classexam":classexam,
            "homework":homework,
            "classcall":classcall,
            "user_memo":user_memo,
            "comment_id":1,
            "object_type": "normal"
        }

        $("#send_comment_button").attr('disabled', true);
        rest_post_keywords_comment(body,function(result){
            console.log(result)
            if(result == "ok"){

            }else{
                alert("error");
            }
            window.location.reload();
        });
    }
});