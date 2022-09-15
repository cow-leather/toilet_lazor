const axios = require('axios').create()
export const req1 = async function(){
    const response = await axios.get("/api/req")
    return response.data
}