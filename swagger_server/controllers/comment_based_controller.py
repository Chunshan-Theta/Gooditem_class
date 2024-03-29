import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.util_mysql import comment_operation
from swagger_server.controllers.util_request import header



def info_class_with_array_obj_input(comment_id):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    """Info of class

     # noqa: E501

    :param comment_id: Eamples: 1
    :type comment_id: int

    :rtype: object
    """
    c = comment_operation()
    return c.select_comment_byid(comment_id=comment_id).to_dict(),200,header

def delete_class_with_array_obj_input(comment_id):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    """Info of class

     # noqa: E501

    :param comment_id: Eamples: 1
    :type comment_id: int

    :rtype: object
    """
    try:
        c = comment_operation()

        c.delete_comment_byid(comment_id=comment_id)
        return Message(msg="ok").to_dict(), 200,header
    except Exception as e:
        return Message(request_status="error",msg="UNKNOWERROR: {}".format(e)).to_dict(), 200,header


def new_class_with_array_obj_input(body):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    """Info of class

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body_json = connexion.request.get_json()
        body = Comment.from_dict(body_json)  # noqa: E501
        try:
            c = comment_operation()
            major = body_json['major'] if 'major' in body_json else "這傢伙很懶，什麼都沒有寫"
            midexam = body_json['midexam'] if 'midexam' in body_json else "這傢伙很懶，什麼都沒有寫"
            endexam = body_json['endexam'] if 'endexam' in body_json else "這傢伙很懶，什麼都沒有寫"
            value = body_json['value'] if 'value' in body_json else "這傢伙很懶，什麼都沒有寫"
            cost = body_json['cost'] if 'cost' in body_json else "這傢伙很懶，什麼都沒有寫"
            classcall = body_json['classcall'] if 'classcall' in body_json else 2
            homework = body_json['homework'] if 'homework' in body_json else 2
            classexam = body_json['classexam'] if 'classexam' in body_json else 2
            _ = c.new_comment_byid(body.class_name, body.teacher_name, major, midexam, endexam, body.user_memo, value, cost,classcall,homework,classexam)

            return Message(msg="ok").to_dict(), 200,header
        except Exception as e:
            return Message(request_status="error", msg="UNKNOWERROR: {}".format(e)).to_dict(), 200,header
    else:
        error_msg = Message(request_status="error", msg="connexion.request.is_json")
        return error_msg.to_dict(),500,header


def update_class_with_array_obj_input(body):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    """Info of class

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501
        return body,200,header
    else:
        error_msg = Message(request_status="error", msg="connexion.request.is_json")
        return error_msg.to_dict(), 500,header

def options_method():
    return {"status":"ok"}, 200, header