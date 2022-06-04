// Objects are hash tables, they store information in a key-value pair.
// They are very similar to dictionaries in Python.

// Unlike an array, a Javascript Object does NOT retain order, instead you access
// the value you want by entering its corresponding key. They can hold a variety of
// data types, including nested Objects.


var carInfo = {
    make: "Toyota",
    year: 1990 ,
    model: "Camry" ,
    carAlert: function(){
      alert('Your car info is, make: '+this.make+ " year: "+this.year+ " model:"+this.model)
    }
  };

// console.dir(document) to get the objects 