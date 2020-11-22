import React,{Component} from 'react';
import {similarTweets} from '../services/service';
//import {similarTweets} from '../services/mock';
import { Link } from "react-router-dom";
import {Menu} from './Menu';




class SimilarUsers extends Component{
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
      console.log(data)
       this.setState({tweets:data,loading:false})
     }
   });
 }

 componentDidMount=()=>{
   const id=this.props.match.params.id
   this.init(id)
 }

 renderTweets=(tweets)=>{     
   console.log(tweets)   
   return(
     <div className="row">
   {tweets.map((tweet,i) => (
     <div className="card col-md-4 mx-2 my-2"  key={i} style={{width: "18rem"}}>           
     <h2>{tweet.username}</h2>    
     <div className="row">
       <div className="col-md-4">

     <Link to={`${tweet.profile_image_url}`}>
     <img className="card-img-top" src={`${tweet.profile_image_url}`}  alt={tweet.user_name}  style={{width:'150px',height:"150px",objectFit:"cover"}}/> 
     </Link>
     </div>
     <div className="col=md-8">      
        <a  href={`http://twitter.com/${tweet.screen_name}`}> Follow {tweet.username} </a>
      </div>                             
     </div>
     <div className="row"></div>
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
   
   <h2 className="mt-2 mb-2">People you may want follow </h2>
   <div className="jumbotron">
   {this.renderTweets(tweets)}
   </div>

   
   </div>
 )
}
}
export default SimilarUsers;