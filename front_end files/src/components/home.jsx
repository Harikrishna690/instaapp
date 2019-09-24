import React from 'react';
import {getStatic, checkLogin, get} from './utilities';
import {Redirect ,Link} from 'react-router-dom';
var imagetags=[];
var j=0,v;
export default class Home extends React.Component {
    constructor(props){
        super(props);
        this.state = {offset: 0, count: 10};
    }

    async UNSAFE_componentWillMount() {
        await get(
            '/data/images/'
        )
        .then(imagedata => imagedata.json())
        .then( async function(imagedata)
        {   
            for(var i=0;i<imagedata.length;i++){
                await get(
                    '/data/liked/?ImageId='+imagedata[i]["id"]
                )
                .then(likeddata=> likeddata.json())
                .then( function(likeddata){
                    if(likeddata[0]=== undefined)
                    {
                        v=<p className="lnostyle">no data</p>;
                    }
                    else
                    {
                        v= <p> Liked by {likeddata[0]["personId"]["username"]} </p>
                        
                    }
                }

                )
                .catch(console.log)
                imagetags.push(
                <div className="card card-block" key={j++}>
                   <div className="media">
                        <div className="media-left">
                            <figure className="image is-48x48">
                            <img 
                            src={imagedata[i]["person_uploaded"]["Image"][0] === '/' ? getStatic(imagedata[i]["person_uploaded"]["Image"]) : imagedata[i]["person_uploaded"]["Image"]}
                            alt="profile" key={j+"image"}/>
                            </figure>
                        </div>
                        <div className="media-content">
                            <p className="title is-4">{imagedata[i]["person_uploaded"]["username"]}</p>
                        </div>
                    </div>
                    <div className="card-image logo-img">
                        <figure className="image is-5by4">
                            <img src={imagedata[i]["Image"][0] === '/' ? getStatic(imagedata[i]["Image"]) : imagedata[i]["Image"]}
                            key={i}
                            alt="give the proper url"/>
                        </figure> 
                    </div>
                    <div className="like">
                        <i className="far fa-heart"></i>
                    </div>
                    <div className="like">
                        <i className="far fa-comment"></i>
                    </div>
                    <div className="like">
                        <i className="fas fa-share"></i>
                    </div>
                    <div className="card-content">
                        <a href="/profiledata"><b className="pstyle">{imagedata[i]["person_uploaded"]["username"]}</b></a>
                        <p className="pstyle">&nbsp;{imagedata[i]["description"]}</p>
                            <div className=""> 
                                <br/>            
                                <b>{v}</b>
                            </div>                       
                    </div>
                </div>
                
                );
            }
        })
        .catch(console.log)
        this.setState({
            images:imagetags,
            isLoggedIn: await checkLogin(),
        });
    }


getprofile() {
        return <Redirect to="/profile" />
  }

async getinputdata(event){
    if(event.keyCode === 13){
        const name= document.getElementById("input").value;
        await get(
            '/data/user/?username='+name,
            {'Content-Type' : 'application/json'}
        )
        .then(data=>data.json())
        .then(console.log)
        .catch(console.log)
    }
}
    render() {
        if(this.state['isLoggedIn']){
            return  (
        <div className="container">
            <div className="setitems">
                <img className="imgset" src={getStatic("/index.png")}
                    alt="Placeholder"/>
                <span className = "logo-text">
                    Instagram 
                </span>
                <input 
                    className="input is-warning is-rounded search-box" 
                    type="text" 
                    onKeyDown={this.getinputdata} 
                    placeholder="search" 
                    id="input"
                />
                <Link to="/profile">
                    <img className="imgset" src={getStatic("/images.png")} 
                        alt="Placeholder" />
                </Link>
            </div>
            <div className="cardset">
                {this.state.images}
            </div>
        </div>
            );    
        }   else    {
            // Redirect To Login
            return (<div>You are not logged in</div>);
        }

    } 
}
