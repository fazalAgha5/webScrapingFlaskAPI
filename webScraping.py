import requests
from bs4 import BeautifulSoup
from flask import Flask,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def test():
  #print(getTheAgeNews())
  data = {"the_age_news": getTheAgeNews(),"the_austrailian_news":getTheAustralianNews()}
  print(data)
  # data = {"the_age_news":{"headlines":["asdfjaksjdfsa f","cvbcvb"],"news":["1321313132231313212","asdfasdfasdfsadf"]},
  # "the_austrailian_news":{"headlines":["index","asdfjak55"],"news":["aaa132sa3d2f2d","bbbasdfasdfasfd"]}}
  return jsonify(data)



def getTheAgeNews():
  url="https://www.theage.com.au"
  page = requests.get(url) 
  soup = BeautifulSoup(page.content, 'html.parser')
  section=soup.find(class_="DF6D8")
  topNews=section.find_all(class_="_1YzQk")
  heading=[item.find("h3").get_text() for item in topNews];
  news=[item.find(class_="_3XEsE").get_text() for item in topNews]
  value={"headlines":heading,"news":news}
  return value


def getTheAustralianNews():
  url="https://www.theaustralian.com.au/"
  page = requests.get(url) 
  soup = BeautifulSoup(page.content, 'html.parser')
  # section=soup.find(class_="area subarea-1 item  ipos-1 irpos-3")
  heading=[]
  news=[]
  for x in range(8):
    post=soup.find(class_="pos pos"+str(x+2))
    heading.append(post.find(class_="story-block__heading").get_text())
    try:
      news.append(post.find(class_="story-block__standfirst").get_text())  
    except:
      print("")
      heading.pop()
    value={"headlines":heading,"news":news}
  return value


  if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

# getTheAgeNews("https://www.theage.com.au")
#getTheAustralianNews("https://www.theaustralian.com.au/")
