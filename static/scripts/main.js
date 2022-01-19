$(function() {
  //Translate text with flask route
  $("#translate").on("click", function(e) {
    e.preventDefault();
    var detectLanguage = ""
    var translateVal = document.getElementById("text-to-translate").value;
    var languageVal = document.getElementById("select-language").value;
    var translateRequest = { 'text': translateVal, 'to': languageVal, 'from': detectLanguage }
    var detectRequest = { 'text': translateVal}

    if (translateVal !== "") {
      $.ajax({
        async: false,
        url: '/detect-text',
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        dataType: 'json',
        data: JSON.stringify(detectRequest),
        success: function(data) {
            detectLanguage = data.detectedLanguage.iso6391Name
            switch(detectLanguage){
              case 'zh_cht':
                detectLanguage = 'zh-Hant'
                break;
              case 'zh_chs':
                detectLanguage = 'zh-Hans'
                break;
            }
            translateRequest.from = detectLanguage
            document.getElementById("detected-language-result").textContent = data.detectedLanguage.name;
            if (document.getElementById("detected-language-result").textContent !== ""){
              document.getElementById("detected-language").style.display = "block";
            }
            document.getElementById("confidence").textContent = data.detectedLanguage.confidenceScore;
          }
      });

    if (detectLanguage !== "")
    {
      $.ajax({
        url: '/translate-text',
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        dataType: 'json',
        data: JSON.stringify(translateRequest),
        success: function(data) {
          for (var i = 0; i < data.length; i++) {
            document.getElementById("translation-result").textContent = data[i].translations[0].text;
            document.getElementById("detected-language-result").textContent = data[i].detectedLanguage.language;
            if (document.getElementById("detected-language-result").textContent !== ""){
              document.getElementById("detected-language").style.display = "block";
            }
            document.getElementById("confidence").textContent = data[i].detectedLanguage.score;
          }
        }
      });
    }
    };
  });
  //Run sentinment analysis on input and translation.
  $("#sentiment-analysis").on("click", function(e) {
    e.preventDefault();
    var inputText = document.getElementById("text-to-translate").value;
    var inputLanguage = document.getElementById("detected-language-result").innerHTML;
    var outputText = document.getElementById("translation-result").value;
    var outputLanguage = document.getElementById("select-language").value;

    var sentimentRequest = { "inputText": inputText, "inputLanguage": inputLanguage, "outputText": outputText, "outputLanguage": outputLanguage };

    if (inputText !== "") {
      $.ajax({
        url: '/sentiment-analysis',
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        dataType: 'json',
        data: JSON.stringify(sentimentRequest),
        success: function(data) {
          for (var i = 0; i < data.documents.length; i++) {
            if (typeof data.documents[i] !== 'undefined'){
              if (data.documents[i].id === "1") {
                document.getElementById("input-sentiment").textContent = data.documents[i].score;
              }
              if (data.documents[i].id === "2") {
                document.getElementById("translation-sentiment").textContent = data.documents[i].score;
              }
            }
          }
          for (var i = 0; i < data.errors.length; i++) {
            if (typeof data.errors[i] !== 'undefined'){
              if (data.errors[i].id === "1") {
                document.getElementById("input-sentiment").textContent = data.errors[i].message;
              }
              if (data.errors[i].id === "2") {
                document.getElementById("translation-sentiment").textContent = data.errors[i].message;
              }
            }
          }
          if (document.getElementById("input-sentiment").textContent !== '' && document.getElementById("translation-sentiment").textContent !== ''){
            document.getElementById("sentiment").style.display = "block";
          }
        }
      });
    }
  });
});
