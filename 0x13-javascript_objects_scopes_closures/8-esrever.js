#!/usr/bin/node
// returns reversed list of an array

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = 0; i < list.length; i++) {
    reversedList[i] = list[(list.length - 1) - i];
  }
  return reversedList;
};
