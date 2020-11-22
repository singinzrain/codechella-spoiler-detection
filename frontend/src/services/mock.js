let tweets =[
    {
      "tweet": `This is actually the most moving scene. Jon and Ghost will live happily together with their fellow wildlings.\n
      I'm still kinda frozen by the finale though.\n
      #Spoilers\n
      The Three-Eyed Raven, King?\n
      Arya as the next Columbus?\n
      Bronn... Master of Coins? Seriously?\n
      #GameOfThrones #GOT\n`,
      "id": 1,
      "isSpoiler": true
      
    },
    {
      "tweet": `If #olly would be in #breakingbad
      #got #jonsnow #hbo #teamnightsking #jonsnowdeath #spoiler #gotseason5c`,
      "id": 2,
      "isSpoiler": false
      
    },
    {
      "tweet": `I’m only a few chapters in so far, but I love it already Pleading 
      face the plot comes from the idea, what if the avengers like the hulk better 
      than bruce? also there’s some Loki whump too!`,
      "id": 3,
      "isSpoiler": false
      
    },
    {
      "tweet": `#GameOfThrones #GoT #Spoilers 

      FireFire The Dragon Queen FireFire
      
      I would have liked that the series took it's time to build up to Danny turning "evil", but I enjoyed Emilia's performance anyways`,
      "id": 4,
      "isSpoiler": true
      
    },
    {
      "tweet": `#CallOfDutyBlackOpsColdWar got me in a cold war/espionage mood. 

      Bridge of Spies (2015) - Steven Spielberg
      
      #film #movie1`,
      "id": 5,
      "isSpoiler":false
      
    },
    {
      "tweet": `Beyond Excited ❣  My #Fantasy & #YAFantasy #books are going to be available to #Stream on #ROKU!  

      #readingcommunity #NextChapterPub #ian1 #IARTG #writerscommunity #Movie #BreakingNews 
      
      https://cynthiaamorganauthor.com`,      
      "id": 6,
      "isSpoiler": true
      
    }
  ]

  let SimilarTweets =[
    {
      "tweet": `This is actually the most moving scene. Jon and Ghost will live happily together with their fellow wildlings.\n
      I'm still kinda frozen by the finale though.\n
      #Spoilers\n
      The Three-Eyed Raven, King?\n
      Arya as the next Columbus?\n
      Bronn... Master of Coins? Seriously?\n
      #GameOfThrones #GOT\n`,
      "id": 8,
      "isSpoiler": true
      
    },
    {
      "tweet": `Beyond Excited ❣  My #Fantasy & #YAFantasy #books are going to be available to #Stream on #ROKU!  

      #readingcommunity #NextChapterPub #ian1 #IARTG #writerscommunity #Movie #BreakingNews 
      
      https://cynthiaamorganauthor.com`,      
      "id": 9,
      "isSpoiler": true
      
    }
  ]  

let sample =
  
[
  {
      "created_at": "Sat, 21 Nov 2020 23:34:27 GMT",
      "id": "1330293528820391936",
      "profile_image_url": "http://pbs.twimg.com/profile_images/1318082537231732737/L_wZh66G_normal.jpg",
      "screen_name": "joshynexttdoor",
      "text": "RT @JeffBarker_: UCLA QB Chase Griffin (@ChaseQB11) throws his first career college TD right as the announcers were showing some love for H…",
      "user_id": "887134615911235584",
      "username": "jo$hua gonzales"
  },
  {
      "created_at": "Sat, 21 Nov 2020 23:35:34 GMT",
      "id": "1330293810304311298",
      "profile_image_url": "http://pbs.twimg.com/profile_images/1316559186797359104/PxYqn80V_normal.jpg",
      "screen_name": "lilcalal",
      "text": "College football keeps slipping down my favorite sports rankings and this Aztecs game is not helping.",
      "user_id": "260495483",
      "username": "Allan May"
  },
  {
      "created_at": "Sat, 21 Nov 2020 23:36:38 GMT",
      "id": "1330294076944625664",
      "profile_image_url": "http://pbs.twimg.com/profile_images/1286134014999330818/-pjQh7sk_normal.jpg",
      "screen_name": "DavidKaufer",
      "text": "Shough needs to see that blitz coming and get rid of the ball quicker. Bruins have done so much damage with those blitzes today.",
      "user_id": "14875084",
      "username": "David Kaufer"
  },
  {
    "created_at": "Sat, 21 Nov 2020 23:36:38 GMT",    
    "id":1330252779164753922,    
    "profile_image_url":"http://pbs.twimg.com/profile_images/1307086490116198401/Cme7kKGb_normal.jpg",
    "screen_name":"Hummmmmbaby",    
    "text":"RT @TwitterU: If you are attending #Codechella 🎡 from your house are you @ Couchchella or Codechilling?",    
    "user_id":289483672,      
    "username":"Kelly 🎡 is at #Codechella"     
  }
]
  
let similar =
  
[
  {
    "created_at":"Sat Nov 21 20: 52: 32 +0000 2020",
    "id":1330252779164753922,    
    "profile_image_url":"https://pbs.twimg.com/profile_images/1307086490116198401/Cme7kKGb_normal.jpg",
    "screen_name":"Hummmmmbaby",
    "text":"RT @TwitterU: If you are attending #Codechella 🎡 from your house are you @ Couchchella or Codechilling?",
    "user_id":289483672,    
    "username":"Kelly 🎡 is at #Codechella"

    

  },
  {
      "created_at": "Sat, 21 Nov 2020 23:35:34 GMT",
      "id": "1330293810304311298",
      "profile_image_url": "http://pbs.twimg.com/profile_images/1316559186797359104/PxYqn80V_normal.jpg",
      "screen_name": "lilcalal",
      "text": "College football keeps slipping down my favorite sports rankings and this Aztecs game is not helping.",
      "user_id": "260495483",
      "username": "Allan May"
  }
]
  export let list = () => new Promise(resolve => resolve(sample));
  
  export let similarTweets = (id) => new Promise(resolve => resolve(similar));