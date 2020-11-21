 import React,{Component} from 'react';
 import {similarTweets} from '../services/mock';
 import { Link } from "react-router-dom";
 import {Menu} from './Menu';

 


class SimilarTweets extends Component{
  constructor(){
    super()
    this.state={
      tweets:[],
      loading:false
    }
  }

  init=(id)=>{
    this.setState({loading:true});    
    similarTweets(id) 
    .then(data =>{
      if(data.error){
          console.log(data.error)
        }
      else{        
        this.setState({tweets:data,loading:false})
      }
    });
  }

  componentDidMount=()=>{
    const id=this.props.match.params.id
    this.init(id)
  }

  renderTweets=(tweets)=>{     
    return(
      <div className="row">
    {tweets.map((tweet,i) => (
      <div className="card col-md-4"  key={i} style={{width: "17rem"}}>       
        <div className="card-body">
          <h5 className="card-title">{tweet.id}</h5>
          <p className="card-text">{tweet.tweet}</p>                   
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
        <div className="text-center">
            <h2>Loading...</h2>
        </div>
    ) : (
        ""
    )}
    
    <h2 className="mt-2 mb-2">Similar Tweets </h2>
    <div className="jumbotron">
    {this.renderTweets(tweets)}
    </div>

    
    </div>
  )
}
}
export default SimilarTweets;