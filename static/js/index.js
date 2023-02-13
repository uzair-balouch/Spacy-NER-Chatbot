

    const msgerForm = get(".msger-inputarea");
    const msgerInput = get(".msger-input");
    const msgerChat = get(".msger-chat");



    // Icons made by Freepik from www.flaticon.com
    const BOT_IMG = "/static/images/bot.png";
    const PERSON_IMG = "/static/images/personImage.svg";
    const BOT_NAME = "Keeton (The Bot)";
    const PERSON_NAME = "Uzair";

    msgerForm.addEventListener("submit", event => {
      event.preventDefault();

      const msgText = msgerInput.value;
      if (!msgText) return;

      appendMessageUnOrderList(PERSON_NAME, PERSON_IMG, "right", msgText);

      msgerInput.value = "";

      botResponse(msgText);
    });



const sayHiButton = get("#sayHi");
function sayHi(){
  console.log("sayHi");
  var salam = "Salam";
  appendMessageUnOrderList(PERSON_NAME, PERSON_IMG, "right", salam);
  const sayHiValue = sayHiButton.value;
  if (!sayHiValue) return;
  appendMessageUnOrderList(BOT_NAME, BOT_IMG, "left", sayHiValue);
  speak(sayHiValue);
  nameCall();
  msgerChat.scrollTop += 500;
};






function appendMessageUnOrderList(name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
<div class="msg ${side}-msg">
<div class="msg-img" style="background-image: url(${img})"></div>

<div class="msg-bubble" id="expand-bubble">
  <div class="msg-info">
    <div class="msg-info-name">${name}</div>
    <div class="msg-info-time">${formatDate(new Date())}</div>
  </div>

  <div class="msg-text">${text}</div>
</div>
</div>
`;

    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;

    //msgerChat.scrollToBottom += 500;
    //msgerChat.animate({scrollTop: $(".msger-chat").height()}, 1000);


  }





    // Put your Javascript Here
    // Name Data List
    var dataList = []
    console.log(dataList)

    const width = 1349;

//Database Response Text Array
DataBaseResponse = [];


function botResponse(msg) {
  console.log("===================")
  console.log(msg)
  console.log("===================")

  // Bot Response
  $.get("/get", { msg: msg }).done(function (data) {
    console.log('I am here Bot Response');
    console.log(data);
    console.log("INside BOT RESPONSE START");
    const msgText = data;
    var listData  = dataList.push(msg);
    console.log(dataList);
    console.log(listData);
    var listData  = dataList.push(msgText);
    console.log("Inside else");
    appendMessageUnOrderList(BOT_NAME, BOT_IMG, "left", msgText);
    speak(msgText);
  
  });
}


    // Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}

function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
};




//    Working Code of Voices Excellent Working END From Here


