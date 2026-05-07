from flask import Blueprint,request,jsonify,render_template
from app.services.llm_services import get_ai_response

chat_bp = Blueprint('/chat',__name__)

@chat_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@chat_bp.route("/chat",methods=["POST"])

def chat():
    data =request.get_json()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",data)
    user_message = data.get("message")
    print("#########################",user_message)
    
    if not user_message:
        return jsonify({
            "error":"Message is required"
        }),400
      
    ai_response = get_ai_response(user_message)
    
    return jsonify({
        "user_message":user_message,
        "ai_response":ai_response
    })    
        