let branchProducerBtn = document.querySelector("#branch-btn");
let branchProducerInput = document.querySelector("#branch-input")

let handleBranchProducer = () => {
    count = branchProducerInput.value;
    console.log(count)
}

branchProducerBtn.addEventListener("click", ()=> handleBranchProducer());