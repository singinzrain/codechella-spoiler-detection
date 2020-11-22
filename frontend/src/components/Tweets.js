 import React,{Component} from 'react';
 //import {list} from '../services/mock';
 import {list} from '../services/service';
 import { Link } from "react-router-dom";
 
class Tweets extends Component{
  constructor(){
    super()
    this.state={
      tweets:[],
      loading:false
    }
  }

  componentDidMount=()=>{
    this.setState({loading:true});    
    list()
    .then(data =>{
      if(data.error){
          console.log(data.error)
        }
      else{
        // console.log("data:",data  )
        this.setState({tweets:data,loading:false})
      }
    })
  }


  renderTweets=(tweets)=>{     
    return(
      <div className="row">
  

    {tweets.map((tweet,i) => (
      <div className="card col-md-4  mx-2 my-2"   key={i} style={{width: "16rem"}}>       
        <div className="card-body">          
          <p className="card-text">{tweet.text}</p>              
      </div>
      <div className="row">      
          <Link className="btn btn-raised btn-primary btn-sm col-md-4 offset-md-4" to={`/similar/${tweet.id}}`}>View Similar Tweets</Link>                  
      </div>
      <p className="font-italic mark ">PostedBy: <a  href={`http://twitter.com/${tweet.screen_name}`}> {tweet.username} </a> on {new Date(tweet.created_at).toDateString()}</p></div> 
    ))}
    </div>
  )
}


render(){
  const {tweets,loading}=this.state;
  console.log(tweets)
  return(
    <div>
    {loading ? (
        <div className="jumbotron text-center">
            <h2>Loading...</h2>
        </div>
    ) : (
        ""
    )}
    <div className="jumbotron">
    
      {this.renderTweets(tweets)}
    </div>
    </div>
  )
}

}



// export const Tweets= () => (
//   <div>
//   <div className="jumbotron">
//   <h2>Home</h2>
//   <p className="lead">Tweets</p>
//   </div>
//   </div>
// )

export default Tweets;