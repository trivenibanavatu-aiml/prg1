(() => {
  const boardEl = document.getElementById('board');
  const statusEl = document.getElementById('status');
  const restartBtn = document.getElementById('restart');
  const aiToggle = document.getElementById('aiToggle');
  const scoreXEl = document.getElementById('scoreX');
  const scoreOEl = document.getElementById('scoreO');

  const WIN_COMBOS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
  ];

  let board = Array(9).fill('');
  let current = 'X';
  let running = true;
  let scores = { X: 0, O: 0 };

  // load scores
  try{ const s = JSON.parse(localStorage.getItem('ttt-scores')); if(s?.X!=null) scores=s; }catch(e){}
  scoreXEl.textContent = scores.X;
  scoreOEl.textContent = scores.O;

  function updateStatus(msg){ statusEl.textContent = msg }

  function render(){
    boardEl.querySelectorAll('.cell').forEach(btn => {
      const i = Number(btn.dataset.index);
      btn.textContent = board[i];
      btn.disabled = !running || board[i] !== '';
    });
  }

  function checkWin(player){
    return WIN_COMBOS.some(combo => combo.every(i => board[i] === player));
  }

  function checkDraw(){ return board.every(Boolean); }

  function endRound(winner){
    running = false;
    if(winner){
      updateStatus(`Player ${winner} wins!`);
      scores[winner]++;
      scoreXEl.textContent = scores.X;
      scoreOEl.textContent = scores.O;
      localStorage.setItem('ttt-scores', JSON.stringify(scores));
    } else {
      updateStatus("It's a draw.");
    }
    render();
  }

  function playerMove(i){
    if(!running || board[i]) return;
    board[i] = current;
    if(checkWin(current)) return endRound(current);
    if(checkDraw()) return endRound(null);
    current = current === 'X' ? 'O' : 'X';
    updateStatus(`Player ${current}'s turn`);
    render();

    // if AI enabled and it's O's turn
    if(aiToggle.checked && current === 'O'){
      // small delay for feel
      setTimeout(aiMove, 300);
    }
  }

  function aiMove(){
    // try win, then block, else random
    const move = findBestMove('O') ?? findBestMove('X') ?? randomMove();
    if(move==null) return;
    board[move] = 'O';
    if(checkWin('O')) return endRound('O');
    if(checkDraw()) return endRound(null);
    current = 'X';
    updateStatus(`Player ${current}'s turn`);
    render();
  }

  function findBestMove(player){
    for(let i=0;i<9;i++){
      if(!board[i]){
        board[i] = player;
        const wins = checkWin(player);
        board[i] = '';
        if(wins) return i;
      }
    }
    return null;
  }

  function randomMove(){
    const avail = board.map((v,i)=> v ? -1 : i).filter(i=>i>=0);
    if(!avail.length) return null;
    return avail[Math.floor(Math.random()*avail.length)];
  }

  // events
  boardEl.addEventListener('click', e => {
    if(!e.target.classList.contains('cell')) return;
    const idx = Number(e.target.dataset.index);
    playerMove(idx);
  });

  restartBtn.addEventListener('click', () => {
    board = Array(9).fill('');
    current = 'X';
    running = true;
    updateStatus(`Player ${current}'s turn`);
    render();
  });

  aiToggle.addEventListener('change', () => {
    // if enabling AI and it's O's turn and board empty or it's O's turn, let AI play
    if(aiToggle.checked && current === 'O' && running){
      setTimeout(aiMove, 300);
    }
  });

  // init
  updateStatus(`Player ${current}'s turn`);
  render();

})();
