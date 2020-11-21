 import React,{Component} from 'react';
 import {list} from '../services/mock';
 //import {list} from '../services/service';
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
      <div className="card col-md-4"  key={i} style={{width: "17rem"}}>       
        <div className="card-body">
          <h5 className="card-title">{tweet.id}</h5>
          <p className="card-text">{tweet.tweet}</p>          
          <Link className="btn btn-raised btn-primary btn-sm" to={`/similar/${tweet.id}}`}>View Similar Tweets</Link>         
        </div>
        
      </div>
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