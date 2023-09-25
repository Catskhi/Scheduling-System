import jwt_decode from 'jwt-decode'
import axios from 'axios'

interface decoded {
    user_id: number
}

export interface userData {
    id: number,
    user_type: number,
    username: string
}

export const getIsLogged = async () => {
    const token = localStorage.getItem('token')
    let isLogged: boolean = true
    await axios.post(getServerUrl() + '/token/verify/', {
        token: token
    })
    .then((response => {
        console.log(response.data)
    }))
    .catch((error) => {
        isLogged = false
        console.log(error.response.data)
    })
    return isLogged
}

export const getUserData = async () => {

    const token = localStorage.getItem('token')
    let userData: userData | undefined
    if (token) {
        const decodedToken: decoded = jwt_decode(token)
        await axios.get(getServerUrl() + '/users/' + decodedToken.user_id + '/')
        .then((response) => {
            userData = response.data
        })
        return userData
    }    
}