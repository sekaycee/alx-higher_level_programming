#!/usr/bin/node
exports.callMeMaybe = function (x, theFunction) {
  theFunction.call(this, x + 1);
};
