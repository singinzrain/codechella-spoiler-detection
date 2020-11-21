import React from 'react'
import Tweets from './Tweets';

export const Home= () => (
  <div>
  <div className="jumbotron">
  <h2>Home</h2>
  <p className="lead">CodeChella</p>
  </div>
  <div className="container-fluid">
    <Tweets />
  </div>
  </div>
)
