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
  
  export let list = () => new Promise(resolve => resolve(tweets));
  
  export let similarTweets = (id) => new Promise(resolve => resolve(SimilarTweets));