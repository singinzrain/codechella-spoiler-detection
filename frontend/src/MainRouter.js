import React from "react";
import { Route, Switch } from "react-router-dom";
import SimilarTweets from './components/SimilarTweets'
import {Home} from './components/Home'
import {Menu} from './components/Menu'

export const MainRouter = () => (
    <div>    
      <Menu />
    <Switch>
    <Route exact path="/tweets" component={Home}></Route>        
    <Route exact path="/similar/:id" component={SimilarTweets} ></Route>    
    <Route exact path="/" component={Home}></Route>
    </Switch>
    </div>
  )
  