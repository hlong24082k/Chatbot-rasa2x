# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

class act_admision_hotline_web(Action):

    def name(self) -> Text:
        return "act_admision_hotline_web"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "postback",
            "title": "Cách tuyển sinh",
            "payload": "Cách tuyển sinh"
        }
        button1 = {
            "type": "postback",
            "title": "Gọi trực tiếp",
            "payload": "Gọi trực tiếp"
        }
        button2 = {
            "type": "web_url",
            "url": "https://dut.udn.vn/tuyensinh2021",
            "title": "Website tuyển sinh"
        }
        ret_text = "Mình có thể giúp gì cho bạn?"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1, button2])

        return []

class more_infor_way1(Action):

    def name(self) -> Text:
        return "more_infor_way1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://thisinh.thithptquocgia.edu.vn/",
            "title": "Đăng ký online"
        }
        ret_text = "Đăng ký hồ sơ tại trường THPT hiện đang học\nLink đăng ký online theo hệ thống của Bộ Giáo dục và Đào tạo"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class way1(Action):

    def name(self) -> Text:
        return "way1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn/Tuyensinh2021/Gioithieu/id/6061",
            "title": "Tuyển theo kết quả thi tốt nghiệp"
        }
        ret_text = "Tổng hợp thông tin về cách xét tuyển bằng điểm thi Tốt nghiệp THPT"
        dispatcher.utter_message(text=ret_text, buttons=[button])
        return []

class way2_front(Action):

    def name(self) -> Text:
        return "way2_front"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn/Tuyensinh2021/Gioithieu/id/6063",
            "title": "Tuyển theo kết quả học bạ"
        }
        ret_text = "Thông tin về cách xét tuyển bằng điểm học bạ THPT."
        dispatcher.utter_message(text=ret_text, buttons=[button])
        return []
        



class more_infor_way2(Action):

    def name(self) -> Text:
        return "more_infor_way2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
           "type": "web_url",
            "url": "http://ts.udn.vn/HBa/RegHDan.aspx?iddot=69&madot=8987",
            "title": "Tuyển sinh online"
        }
        ret_text = "Cổng đăng ký xét tuyển online ĐH Bách khoa Đà Nẵng."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []        

class way3(Action):

    def name(self) -> Text:
        return "way3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
           "type": "web_url",
            "url": "http://dut.udn.vn/Tuyensinh2021/Gioithieu/id/6064",
            "title": "Tuyển bằng điểm thi ĐGNL"
        }
        ret_text = "Thông tin về cách xét tuyển bằng Điểm kỳ thi ĐGNL ĐH Quốc gia Tp.HCM"
        dispatcher.utter_message(text=ret_text, buttons=[button])
        return []

class more_infor_way3(Action):

    def name(self) -> Text:
        return "more_infor_way3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://thinangluc.vnuhcm.edu.vn/dgnl/home.action",
            "title": "Kỳ thi ĐGNL ĐHQG-HCM"
        }
        button1 = {
            "type": "web_url",
            "url": "http://ts.udn.vn/",
            "title": "Đk Online"
        }
        ret_text = "Link thông tin về kỳ thi đánh giá năng lực ĐHQG-HCM"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1])

        return []

class way4(Action):

    def name(self) -> Text:
        return "way4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn/Tuyensinh2021/Gioithieu/id/6060",
            "title": "Tuyển sinh riêng"
        }
        ret_text = "Thông tin về cách xét tuyển sinh riêng."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class more_infor_way4(Action):

    def name(self) -> Text:
        return "more_infor_way4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn/tuyensinh2021",
            "title": "ĐK online"
        }
        ret_text = "Có thể đăng kí online tại đây."
        dispatcher.utter_message(text=ret_text, buttons=[button])
        return []

class link_fanpage(Action):

    def name(self) -> Text:
        return "link_fanpage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://www.facebook.com/DUTpage",
            "title": "Fanpage Đại học Bách khoa Đà Nẵng"
        }
        ret_text = "Link Fanpage chính thức về thông tin tuyển sinh ĐH DUT. Bạn có thể theo dõi fanpage để cập nhật những thông tin nhanh và chính xác nhất về tuyển sinh."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class main_link(Action):

    def name(self) -> Text:
        return "main_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://dut.udn.vn/",
            "title": "Website ĐH Bách khoa Đà Nẵng."
        }
        ret_text = "Link website chính thức của trường"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class admission_link(Action):

    def name(self) -> Text:
        return "admission_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://dut.udn.vn/Tuyensinh2021",
            "title": "Trang tuyển sinh"
        }
        ret_text = "Link trang tuyển sinh trường Đại học Bách khoa Đà Nẵng."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class more_informajor_2021mark(Action):

    def name(self) -> Text:
        return "more_informajor_2021mark"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://www.thongtintuyensinh.vn/Diem-chuan-nam-2020-cua-Truong-Dai-hoc-Bach-khoa-DH-Da-Nang_C237_D16959.htm",
            "title": "Thông tin chi tiết"
        }
        ret_text = "Thông tin về ngành và điểm năm 2020"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class link_register_online(Action):

    def name(self) -> Text:
        return "link_register_online"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://dut.udn.vn/Tuyensinh2021/Thongbao/id/6261",
            "title": "Thông tin xét tuyển trực tiếp"
        }
        button1 = {
            "type": "web_url",
            "url": "https://www.facebook.com/DUTpage",
            "title": "Fanpage của trường"
        }
        ret_text = "Cổng đăng ký xét tuyển online ĐH Bách khoa Đà Nẵng.\nBạn cũng có thể theo dõi fanpage bên dưới để cập nhật thông tin liên tục."
        dispatcher.utter_message(text=ret_text, buttons=[button, button1])

        return []

class link_form_regis(Action):

    def name(self) -> Text:
        return "link_form_regis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://dut.udn.vn/Tuyensinh2021/Thongbao/id/6261",
            "title": "Thông tin chi tiết"
        }
        ret_text = "Thông tin đăng ký xét truyển trực tuyến ĐH Bách khoa Đà Nẵng."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class act_admission_ways(Action):

    def name(self) -> Text:
        return "act_admission_ways"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Trường ĐH Sư phạm Kỹ thuật có 4 cách tuyển sinh\nCách 1: Xét tuyển theo học bạ THPT\nCách 2: Xét tuyển theo kết quả thi tốt nghiệp\nCách 3: Xét tuyển theo kết quả DDGNL-TP HCM\nCách 4: Phương thức tuyển sinh riêng",
            "quick_replies": [
                
                {
                    "content_type": "text",
                    "title": "Điểm xét học bạ",
                    "payload": "Điểm xét học bạ",
                },
                {
                    "content_type": "text",
                    "title": "kết quả thi tốt nghiệp",
                    "payload": "kết quả thi tốt nghiệp",
                },
                {
                    "content_type": "text",
                    "title": "kết quả DGNL-TP HCM",
                    "payload": "kết quả DGNL-TP HCM",
                },
                {
                    "content_type": "text",
                    "title": "Tuyển sinh riêng",
                    "payload": "Tuyển sinh riêng",
                }
            ]
        }

        dispatcher.utter_message(json_message=message)

        return []

class act_contact_hotline(Action):

    def name(self) -> Text:
        return "act_contact_hotline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "phone_number",
            "title": "0702415105",
            "payload": "0702415105"
        }
        button1 = {
            "type": "phone_number",
            "title": "0987654321",
            "payload": "0987654321"
        }
        ret_text = "Bạn có thể gọi điện thoại trực tiếp vào hai đầu số này"

        dispatcher.utter_message(text=ret_text, buttons=[button, button1])

        return[]

class to_roi(Action):

    def name(self) -> Text:
        return "to_roi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin xét tuyển trường Đại học Bách khoa Đà Nẵng:",
                                 image="http://dut.udn.vn/Images/Slides/Slider_Tuyensinh2021_2.jpg")
        return []

class basic_infor_about_ute_university(Action):

    def name(self) -> Text:
        return "basic_infor_about_ute_university"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn",
            "title": "Trang chủ"
        }
        button1 = {
            "type": "web_url",
            "url": "http://dut.udn.vn/tuyensinh2021",
            "title": "Trang tuyển sinh"
        }
        button2 = {
            "type": "web_url",
            "url": "https://www.facebook.com/DUTpage",
            "title": "Fanpage tuyển sinh"
        }
        ret_text = "Bạn có thể xem những thông tin cơ bản về trường tại các website chính thức của trường:"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1, button2])

        return []

class goodbye(Action):

    def name(self) -> Text:
        return "goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://media.tenor.com/images/e955f55bab6839ec724531e3bae3303c/tenor.gif")

        return []

class info_exam(Action):

    def name(self) -> Text:
        return "info_exam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin về kỳ thi tốt nghiệp THPT 2021",
                                 image="https://hoigiasudanang.com/wp-content/uploads/2021/06/2.-Moc-Thoi-gian-1536x1087.jpg")

        return []

class action_fee(Action):

    def name(self) -> Text:
        return "action_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://reviewedu.net/hoc-phi-truong-dai-hoc-bach-khoa-da-nang-moi-nhat#:~:text=N%C4%83m%202020%2C%20m%E1%BB%A9c%20h%E1%BB%8Dc%20ph%C3%AD,%2Fsinh%20vi%C3%AAn%2Fn%C4%83m%20h%E1%BB%8Dc.",
            "title": "Thông tin học phí"
        }
        ret_text = "ĐH Bách khoa Đà Nẵng là trường đại học công lập, học phí khoảng 5-6 triệu đồng/học kỳ. Bạn có thể tham khảo thêm thông tin về học phí tại đây"
        dispatcher.utter_message(text=ret_text,image="https://media.kenhtuyensinh.vn/images/cms/2020/08/bkdn.png", buttons=[button])

        return []

class act_have_domitory(Action):

    def name(self) -> Text:
        return "action_have_domitory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn/Tuyensinh2021/Thongbao/id/6053",
            "title": "Các thông tin về KTX"
        }
        ret_text = "Trường có KTX ngay cạnh trường và dưới đây là thông tin về KTX của trường nha."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []  

class action_student_support(Action):

    def name(self) -> Text:
        return "action_student_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn/Tuyensinh2019/Gioithieu/id/2912",
            "title": "Thông tin học bổng"
        }
        
        ret_text = "ĐH SPKT có nhiều chính sách hỗ trợ sinh viên có hoàn cảnh khó khăn và có nhiều loại học bổng khác nhau để hỗ trợ cho sinh viên khó khăn và sinh viên xuất sắc nha bạn."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []
