const axios = require('axios').create()
export const req = async function(){
    const response = await axios.get("/api/req")
    return response
}