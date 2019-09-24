import path from 'path';
import constants from './constants.js';

export function getUrl(url) {
    return '//' + path.join(constants.API_BASE, url); 
}

export function getStatic(url) {
    return path.join(constants.PUBLIC_URL, url)
}

export function getAdditionalHeaders() {
    return {
        'token': constants.TOKEN
    }
}

export function checkLogin(){
    return new Promise((resolve, reject) => {
        fetch(
            getUrl('/userLogin/'),
            {
                method: 'HEAD',
                headers: {
                    ...getAdditionalHeaders()
                }
            }
        )
        .then(res => res.status === 200 ? resolve(true) : reject(false))
        .catch(error => reject(false));
    });
}

export function get(url, headers, extraConf={}){
    return fetch(
        getUrl(url),
        {
            method :'GET',
            headers: {
                ...headers,
                ...getAdditionalHeaders()
            },
            ...extraConf
        }
    )
}

export function post(url, headers, body, extraConf={}){
    return fetch(
        getUrl(url),
        {
            method: 'POST',
            headers: {
                ...headers,
                ...getAdditionalHeaders()
            },
            body: JSON.stringify(body),
            ...extraConf
        }
    )
}
