console.log(verbs)

const quiz = (verbs) => {
    let i = 0
    verb = verbs[i]
    document.getElementById('verbToGuess').textContent = verb.english
    let answers = generate_answers(verb)
}

const generate_answers = verb => {
    let answers = [verb.korean]
    while (answers.length < 4) {
        let answer = parent_verbs[Math.floor(Math.random() * parent_verbs.length)]
        if(!answers.includes(answer.korean)){
            answers.push(answer.korean)
        }
    }
    answers = shuffleArray(answers)
    console.log(answers)
}

const shuffleArray = arr => {
    let newArr = []
    while (newArr.length < 4 ){
        let idx = Math.floor(Math.random() * arr.length)
        newArr.push(arr[idx])
        arr.splice(idx, 1)
    }
    return newArr
}

quiz(verbs)