let branchProducerBtn = document.querySelector("#branch-btn");
let branchProducerInput = document.querySelector("#branch-input")

let handleBranchProducer = () => {
    count = branchProducerInput.value;
    
}

branchProducerBtn.addEventListener("click", ()=> handleBranchProducer());