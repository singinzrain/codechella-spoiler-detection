export const list = () =>{
  console.log(`${process.env.REACT_APP_API_URL}/tweets`)
    return fetch(`${process.env.REACT_APP_API_URL}/tweets`,{
      method:"GET"
    })
    .then( response => {
      return response.json()
    }).catch(err=>console.log(err))
  }

  export const similarTweets = (id) =>{
    return fetch(`${process.env.REACT_APP_API_URL}/similarTweets`,{
      method:"GET"
    })
    .then( response => {
      return response.json()
    }).catch(err=>console.log(err))
  }


