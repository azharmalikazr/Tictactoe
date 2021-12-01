import { newArray } from '@angular/compiler/src/util';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';



export interface Tile {
  color: string;
  cols: number;
  rows: number;
  text: string;
}



@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

  
  isHumanTurn: boolean = true;
  isHumanWinner: boolean = false;
  isComputerWinner: boolean = false;
  isComputerTurn: boolean = true
  isDraw: boolean = false;
  tracker: string[] = new Array(9).fill(null);
  // copyBoardTracker: Array<number | null> = new Array(9).fill(null);

  copyBoardTracker: number[] | null[] = new Array(9).fill(null);
  isMoved: boolean = false;
  isLoaded: boolean = false
  leftcheck: boolean = true

  check = 1;
  newcheck=1;
  humanWins = 0;
  compWins = 0;
  drawCount = 0;
  possibleMove: Number[] = new Array;
  checkDraw = 0;
  value: any = 0
  newValue: number = 0
  serverValue : number = 0
  serverValueWins : number = 0
  moveNo: number = 0
  totalGames:number = -1
  leftunfinished:number = 0



  tiles: Tile[] = [
    { text: '', cols: 1, rows: 1, color: 'lightpink' },
    { text: '', cols: 1, rows: 1, color: 'lightgreen' },
    { text: '', cols: 1, rows: 1, color: 'lightpink' },
    { text: '', cols: 1, rows: 1, color: 'lightgreen' },
    { text: '', cols: 1, rows: 1, color: 'lightblue' },
    { text: '', cols: 1, rows: 1, color: 'lightgreen' },
    { text: '', cols: 1, rows: 1, color: 'lightpink' },
    { text: '', cols: 1, rows: 1, color: 'lightgreen' },
    { text: '', cols: 1, rows: 1, color: 'lightpink' },

  ];

  constructor(private http:HttpClient){
    this.http.post('http://172.17.0.3:7070/', this.temp2 ).subscribe(res => {
          console.log(res)
          this.value = res
          console.log(this.value.GameNo)
          if (this.value.GameNo !=-1){
            this.totalGames = this.value.GameNo + 1
            this.humanWins = this.value.HumanWon
            this.compWins = this.value.ComputerWon
            this.drawCount = this.value.Draw
            this.leftunfinished = this.value.Left
            this.isLoaded = true
          }
          else{
            this.totalGames = 1
            this.humanWins = 0
            this.compWins = 0
            this.drawCount = 0
            this.leftunfinished = 0
            this.isLoaded = true
          }

          },(err) => {
          console.log(err)
          })
  }

  


  ngOnInit(): void {
  }
  


  async setMove(index: number): Promise<void> {
     
    
    this.isHumanWinner = false
    this.isComputerWinner = false 
    console.log("hello") 
    

    if (this.isHumanTurn && this.tracker[index] == null) {

      this.tracker[index] = '✓';
      this.tiles[index].text = '✓';
      this.isHumanTurn = false
      this.copyBoardTracker[this.moveNo]=index
      this.moveNo = this.moveNo + 1
      console.log(this.tracker);

      this.checkServerForIndex()
      setTimeout(() => {

        if (this.value.WinnerCheckHuman == 99){
          this.isHumanWinner = true
          this.isHumanTurn = false
          this.humanWins = this.humanWins + 1
          this.temp2['Status of this game'] = "Human Won"
          
          
          setTimeout(() => {
            this.newGame();
            console.log('Human');
          },2000);
        }
        else if (this.value.WinnerCheckHuman == 999){
          this.isDraw = true
          this.isHumanTurn = false
          this.drawCount = this.drawCount +1
          this.temp2['Status of this game'] = "Draw"
          setTimeout(() => {
            this.newGame();
            console.log('Draw');
          },2000);
        }
        else{
          index = this.value.PossibleIndex
          this.tracker[index] = 'X';
          this.tiles[index].text = 'X';
          this.check = this.check + 1;
          this.copyBoardTracker[this.moveNo]=index
          this.moveNo = this.moveNo + 1
          this.isHumanTurn = true
          console.log(this.tracker);
          if (this.value.WinnerCheckComp == 99){
            this.isComputerWinner = true
            this.isHumanTurn = false
            this.compWins = this.compWins + 1
            this.temp2['Status of this game'] = "Computer Won"
            setTimeout(() => {
              this.newGame();
              console.log('Computer');
            },2000);
          }

        }
        console.log(">>>>>>",this.value,"<<<<<")
      }, 50);

    }

       
   
   
    
  }


  

  temp2 = {
    "GameNo" : this.totalGames,
    "Human Won":this.humanWins,
    "Computer Won": this.compWins,
    "Left": this.leftunfinished,
    "Draw": this.compWins,
    "Copy Of Board" : this.copyBoardTracker,
    "Status of this game" : "   "
  }
  temp = {
    "tracker":this.tracker,
    "check": this.check
  }
      
  async checkServerForIndex () {

    this.temp['tracker']=this.tracker
    this.temp['check']=this.check
    console.log(this.temp)

    // console.log(this.temp)
    // let headers = new HttpHeaders().set('access-control-allow-origin','http://127.0.0.1:8022/');
    // console.log(headers+'findMove')
    // console.log(2222)
    let self=this
      await this.http.post('http://172.17.0.4:9090/findMove', this.temp).subscribe(res => {
        // console.log(res)
        this.value = res
      },(err) => {
        console.log(err)
      })
      
      console.log(">>>>>>>>>>",self.value,">>>>>>>>>>>>>>>>>>>")
      return self.value

      // console.log( "ye check index ka hai ",this.newValue)
      // return this.newValue

  }


  



  
 
  
  
  newGame(): void {
    console.log("Initial")

    if (this.tracker[0] != null 
       || this.tracker[1] != null
       || this.tracker[2] != null 
       || this.tracker[3] != null
       || this.tracker[4] != null 
       || this.tracker[5] != null
       || this.tracker[6] != null 
       || this.tracker[7] != null 
       || this.tracker[8] != null){
        this.totalGames = this.totalGames + 1
        this.temp2['GameNo']=this.totalGames
        this.temp2['Human Won']=this.humanWins
        this.temp2['Computer Won']=this.compWins
        this.temp2['Draw']=this.drawCount
        this.temp2['Copy Of Board'] = this.copyBoardTracker
        if (this.isComputerWinner == false && this.isHumanWinner == false && this.isDraw == false){
          this.temp2['Status of this game'] = "Left by Human"
          this.temp2['Left'] = this.leftunfinished+1
          this.leftunfinished = this.leftunfinished+1
          this.leftcheck = false
        }
        
        
        

        this.http.post('http://172.17.0.3:7070/', this.temp2 ).subscribe(res => {
              console.log(res)
               // this.value = res
              },(err) => {
              console.log(err)
            })  
    }

    
      
      
    
    
    setTimeout(() => {
      this.leftcheck = true
  }, 900)
    
    this.isHumanTurn = true
    this.isHumanWinner = false
    this.isComputerWinner = false
    this.isDraw = false;
    this.tracker = new Array(9).fill(null)
    this.copyBoardTracker = new Array(9).fill(null)

    this.moveNo = 0
    this.possibleMove = new Array
    this.check = 1;
    this.temp['tracker']=this.tracker
    this.temp['check']=this.check
    console.log(this.temp)
    for (let i = 0; i < 9; i++) {
      this.tiles[i].text = '';
      
    }

    

    
  }


}