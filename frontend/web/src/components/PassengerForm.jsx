import { React, useState, useEffect} from 'react';
import Select from 'react-select';

function PassengerForm(props) {
   
    const genders = [
        { value: "Male", label: "Mr" },
        { value: "Female", label: "Ms" },

    ]

    const [isClearable, setIsClearable] = useState(true);
    const [isSearchable, setIsSearchable] = useState(true);
    const [isDisabled, setIsDisabled] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [isRtl, setIsRtl] = useState(false);

    const [formData, setFormData] = useState({
        'gender': '',
        'firstName': '',
        'lastName': '',
        'email': '',
        'phone': '' 
    });
    
    const [gender, setGender] = useState("")

    const handleInputChange = (event) => {
        let key, value;

        key = event.target.name;
        value = event.target.value; 

        setFormData({
            ...formData, 
            [key]: value,
            ['gender']: gender['label']
        });

        props.updateContent(props.index, formData); 
    }


    return (
        <div className="passenger-form-wrapper">
            <h1>Passenger {props.index + 1}</h1>
            <div className='passenger-form'>
                <div className="passenger-form-details">
                    <div className="passenger-form-field">
                        <p>Salutation:</p>
                        <Select options={genders}
                            className="passenger-form-select"
                            isDisabled={isDisabled}
                            isLoading={isLoading}
                            isClearable={isClearable}
                            isRtl={isRtl}
                            isSearchable={isSearchable}
                            placeholder="Title"
                            name="gender"
                            value = {gender}
                            onChange={setGender} />
                    </div>
                    <div className="passenger-form-field">
                        <p>First Name:</p>
                        <input
                            name="firstName"
                            type="text"
                            placeholder="Enter your First Name"
                            value = {formData['firstName']}
                            onChange={handleInputChange} 
                        />
                    </div>
                    <div className="passenger-form-field">
                        <p>Last Name:</p>
                        <input
                            name="lastName"
                            type="text"
                            placeholder="Enter your Last Name"
                            value = {formData.lastName}
                            onChange={handleInputChange} 
                        />
                    </div>
                </div>
                <div className="passenger-form-details">
                    <div className="passenger-form-field">
                        <p>Email: </p>
                        <input
                            name="email"
                            type="text"
                            placeholder="Enter your Email"
                            value = {formData.email}
                            onChange={handleInputChange} 
                        />
                    </div>

                    <div className="passenger-form-field">
                        <p>Phone Number: </p>
                        <input
                            name="phone"
                            type="text"
                            placeholder="Enter your Phone Number"
                            value = {formData.phone}
                            onChange={handleInputChange} 
                        />
                    </div>
                </div>
            </div>
        </div>


    )
}



export default PassengerForm;