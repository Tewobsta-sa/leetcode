/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    c = init
    return {
        increment: () => {
            c += 1
            return c
        },
        decrement: () => {
            c -= 1
            return c
        },
        reset : () =>{
            c = init
            return c
        }

    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
