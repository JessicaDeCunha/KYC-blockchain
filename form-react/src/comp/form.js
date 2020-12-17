import React from 'react';
import ReactDOM from 'react-dom';
import './form.css';


class Form extends React.Component{
 constructor(props){
    super(props);
	this.state={
  				fname:'',
  				lname:'',
  				appAddress:'',
  				email:'',
  				phone:''


};

}

ChangeHandler=(event)=>{
var nam=event.target.appname;
var val=event.target.appAddress
this.setState({[nam]: val});
}
// onSubmit=()=>{
// 		fetch(,{
// 		method:"post",
// 		headers:{"Content-type":"applicant/json"},
// 		body:JSON.stringify({

// 			fname:this.state.fname,
// 			lname:this.state.lname,
// 			appAddress:this.state.appAddress,
// 			email:this.state.email,
// 			phone:this.state.phone;
// 			bdate:this.state.bdate,
// 			gender:this.state.gender


// 		})
// 	}
// 	)
// 	}
	render(){
		return(
	<div id='cen'>
	<form id="form">  
	<fieldset>

	<h1>Registration Form</h1>
	
  	<h2>Name of applicant</h2>

	<div id="fullName">
                <input type="text" name="fName" id="fname" placeholder="First Name" required  onChange={this.ChangeHandler}   />
                <input type="text" name="lName" id="lname" placeholder="Last Name" required    onChange={this.ChangeHandler}  />
              </div>

 
   <h2>Address</h2>  
<div id='sub'>   
<input
types= 'address'
name='appAddress'
placeholder="Street Address:"
 required
onChange={this.ChangeHandler}
/>
<input
types= 'email'
name='email'
placeholder='email@gmail.com'
onChange={this.ChangeHandler}
/>
<input
 type="tel"
  name="phone" 
  id="phone"
   placeholder="Telephone Number" 
   required 
   onChange={this.ChangeHandler}
/>

</div>
<br/>
<h2> Date of Birth</h2>
<div id='sub'>  
<input
types= 'date'
name='bdate'
placeholder="MM-DD-YYYY" required
onChange={this.ChangeHandler}
/>
  </div>
  <br/>
   <h2>Gender</h2>
    <div id='sub'> 
<input
types= 'text'
name='gender'
onChange={this.ChangeHandler}
/>
</div>
<br /><br />
              <input
               type="submit"
                name="submit"
                 id="submit"

                 onClick={this.submit}
                  />

</fieldset>
  </form>
  </div>
		)
	}

}
export default Form;