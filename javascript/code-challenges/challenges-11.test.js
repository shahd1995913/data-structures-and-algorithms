'use strict';

/* ------------------------------------------------------------------------------------------------
CHALLENGE 1 - Review

Write a function named transformToLis that, given an object,
returns an array of the key value pairs as html list items.

For example: 
{
  name: 'bob',
  age: 32
}

Becomes: 
[
<li>name: bob</li>,
<li>age: 32</li>
]
------------------------------------------------------------------------------------------------ */
describe('Testing challenge 1', () => {
  test('It should return a list of key value pairs inside of li tags', () => {
    expect(transformToLis({name: 'bob', age: 32})[0]).toStrictEqual(`<li>name: bob</li>`);
    expect(transformToLis({name: 'bob', age: 32})[1]).toStrictEqual(`<li>age: 32</li>`);
    expect(transformToLis({})).toStrictEqual([]);
  });
});


function transformToLis(passedObj){

  // convert the obj to array then render as li
  
  const TheNewArray=[];
  //var object = {1: 'hello', 2: 'world'};
 
  const val = Object.keys(passedObj);
 //var array = Object.values(object);
  for (let m = 0; m < val.length; m++)
   {

    // It should return a list of key value pairs inside of li tags
    TheNewArray.push(`<li>${val[m]}: ${Object.values(passedObj)[m]}</li>`)  

  }
 // return obj.name;
  return TheNewArray
 
  // object.entry  
  // Object.entries().

}

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2

Write a function named count that, given an integer and an array of arrays, uses either filter, map, or reduce to count the amount of times the integer is present in the array of arrays.

Note: You might need to use the same method more than once.

For example, count(5, [[1, 3, 5, 7, 9], [5, 5, 5], [1, 2, 3]]) returns 4.
------------------------------------------------------------------------------------------------ */
describe('Testing challenge 2', () => {
  test('It should return the number of times the input is in the nested arrays', () => {
    expect(count(5, [[1, 3, 5, 7, 9], [5, 5, 5], [1, 2, 3]])).toStrictEqual(4);
    expect(count(3, [[1, 3, 5, 7, 9], [5, 5, 5], [1, 2, 3]])).toStrictEqual(2);
    expect(count(12, [[1, 3, 5, 7, 9], [5, 5, 5], [1, 2, 3]])).toStrictEqual(0);
  });
  test('It should work on empty arrays', () => {
    expect(count(5, [[1, 3, 5, 7, 9], [], [5, 5, 5], [1, 2, 3], []])).toStrictEqual(4);
    expect(count(5, [])).toStrictEqual(0);
  });
});
let count = (val1, val2) => {
  
  

  let  val3 = val2.length;

  let s = 0

  for (let q = 0; q < val3; q++) {
    // The map() method is used for creating a new array from an existing one, applying a function to each one of the elements of the first array.
    val2[q].map(e => 
      {
// const doubled = numbers.map(item => item * 2);
      if (e === val1)
       {
        s++
      }

    }
    
    )

  }
  return s
  // count(5, [[1, 3, 5, 7, 9], [5, 5, 5], [1, 2, 3]]) returns 4.





};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 3

Write a function that, given an array of integer arrays as input, calculates the total sum of all the elements in the array.

You may want to use filter, map, or reduce for this problem, but are not required to. You may need to use the same method more than once.

For example, [[1, 2, 3, 4, 5], [6, 7, 2, 4, 5, 7], [9, 2, 3, 6,]] returns 66.
------------------------------------------------------------------------------------------------ */
describe('Testing challenge 3', () => {
  test('It should add all the numbers in the arrays', () => {
    const nums = [[1, 2, 3, 4, 5], [6, 7, 2, 4, 5, 7], [9, 2, 3, 6,]];

    expect(totalSum(nums)).toStrictEqual(66);
  });
});

let totalSum = (x) =>

{
  let e = x.reduce((c, b) => {
// The reduce() method executes a user-supplied “reducer” callback function on each element of the array,

    return (c += b.reduce((m, m2) => {
// const reducer = (previousValue, currentValue) => previousValue + currentValue;

      return (m += m2);
// reduce(function callbackFn(previousValue, currentValue) { ... })
    }
    ,
     0)
     )
     ;
  }
  ,
   0
   )
   ;
  return e;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 4

Write a function named divisibleByFiveTwoToThePower that accepts an array of arrays as input.

This function should first remove any elements that are not numbers or are not divisible by five.

This function should then raise 2 to the power of the resulting numbers, returning an array of arrays.

For example, [ [0,2,5,4], [2,4,10], [] ] should return [ [1, 32], [1024], [] ].
------------------------------------------------------------------------------------------------ */
describe('Testing challenge 4', () => {
  test('It should return numbers divisible by five, then raise two to the power of the resulting numbers', () => {
    expect(divisibleByFiveTwoToThePower([[10, 20, 5, 4], [5, 6, 7, 9], [1, 10, 3]])).toStrictEqual([[1024, 1048576, 32], [32], [1024]]);
  });

  test('It should return an empty array if none of the numbers are divisible by five', () => {
    expect(divisibleByFiveTwoToThePower([[1, 2, 3], [5, 10, 15]])).toStrictEqual([[], [32, 1024, 32768]]);
  });

  test('It should return an empty array if the values are not numbers', () => {
    expect(divisibleByFiveTwoToThePower([['one', 'two', 'five'], ['5', '10', '15'], [5]])).toStrictEqual([[], [], [32]]);
  });
});
let divisibleByFiveTwoToThePower = (TheInput) => {
  let   Array1 = [];

  TheInput.map((v) => {

    let Array2 = [];

    v.map((y) => {

// This function should first remove any elements that are not numbers or are not divisible by five.

      if (typeof y === "number" && y % 5 === 0) {
        //    if( B[i] % A[j] == 0 )
    
        Array2.push(Math.pow(2, y));
        
        // Array2.push();

        // alert( Array2 );

      }
    });
    Array1.push(Array2);
  });
  return Array1;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 5 

Write a function named findMaleAndFemale that, given the Star Wars data, below,
returns the names of the characters whose gender is either male or female.

The names should be combined into a single string with each character name separated by "and".

For example, "C-3PO and Luke Skywalker".
------------------------------------------------------------------------------------------------ */

describe('Testing challenge 5', () => {
  test('It should return only characters that are male or female', () => {
    expect(findMaleAndFemale(starWarsData)).toStrictEqual('Luke Skywalker and Darth Vader and Leia Organa');
    expect(findMaleAndFemale([{ name: 'person', gender: 'female' }, { gender: 'lol' }, { name: 'persontwo', gender: 'male' }])).toStrictEqual('person and persontwo');
  });
});

let starWarsData = [{
  name: 'Luke Skywalker',
  height: '172',
  mass: '77',
  hair_color: 'blond',
  skin_color: 'fair',
  eye_color: 'blue',
  birth_year: '19BBY',
  gender: 'male',
},
{
  name: 'C-3PO',
  height: '167',
  mass: '75',
  hair_color: 'n/a',
  skin_color: 'gold',
  eye_color: 'yellow',
  birth_year: '112BBY',
  gender: 'n/a'
},
{
  name: 'R2-D2',
  height: '96',
  mass: '32',
  hair_color: 'n/a',
  skin_color: 'white, blue',
  eye_color: 'red',
  birth_year: '33BBY',
  gender: 'n/a'
},
{
  name: 'Darth Vader',
  height: '202',
  mass: '136',
  hair_color: 'none',
  skin_color: 'white',
  eye_color: 'yellow',
  birth_year: '41.9BBY',
  gender: 'male'
},
{
  name: 'Leia Organa',
  height: '150',
  mass: '49',
  hair_color: 'brown',
  skin_color: 'light',
  eye_color: 'brown',
  birth_year: '19BBY',
  gender: 'female'
}];

let findMaleAndFemale = (data) => {

  let Array2 = [];

  data.map(value =>
     {
       // The names should be combined into a single string with each character name separated by "and".


    if (value.gender == 'male' 

    || value.gender == 'female')
     {
      Array2.push(value.name)

      Array2.push(' and ')
    }
  })

  // For example, "C-3PO and Luke Skywalker".
  
  Array2.pop()

  return Array2.join('')
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 6 

Write a function named findShortest that, given the Star Wars data from Challenge 6,
 uses any combination of filter, map and reduce to return the name of the character who is the shortest in height.
------------------------------------------------------------------------------------------------ */

describe('Testing challenge 6', () => {
  test('It should return the name of the shortest character', () => {
    expect(findShortest(starWarsData)).toStrictEqual('R2-D2');
  });
});


const findShortest = (Val) => {

  const Array = [];

  Val.map(t =>
     {

    Array.push(t.height)
// Math.min.apply(Math, Array.map(function(str) {

  }
  
  )
  // Math.min(Array[0].length,Array[1].length,Array[2].length);
  //  Array.reduce(function(r, a) 
  const character = Math.min(...Array)
// result like shortest string between 3 elements of array
  const g = Val.find(t => t.height == character)
// s the shortest in height.
  return g.name
};

/* ------------------------------------------------------------------------------------------------
TESTS

All the code below will verify that your functions are working to solve the challenges.

DO NOT CHANGE any of the below code.

Run your tests from the console: jest challenges-10.test.js

------------------------------------------------------------------------------------------------ */







