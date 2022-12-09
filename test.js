class MainScene extends Phaser.Scene {
    constructor(){ super({ key:'MainScene' }) }
    
    create() {
      
      this.add.text(this.cameras.main.width/2,this.cameras.main.height/2,'ClickMe',{fontSize:52})
        .setOrigin(0.5)
        .setInteractive()
        .on('pointerdown',()=>{
        
        let element = document.getElementById('input-box')
         if(element && element.style.display === 'none') {
                
          element.style.display = 'block';
        
          for (let i = 0; i < element.children.length; i++) {
                      
              // it is an input element
              if(element.children[i].tagName === 'INPUT'){  
                let btn = this.add.text(10,100 + 20*i,'')
                element.children[i].addEventListener('input',()=>{
                  btn.setText(element.children[i].value)            
                })
              }
            
              // it is the button
              else {
                element.children[i].addEventListener('click',()=>{
                  element.style.display = 'none'
                })
              }
          }
        }        
      })   
    }
  }
  
  
  var config = {
      type: Phaser.AUTO,
      scale: {
        parent: 'phaser-example',  
        mode: Phaser.Scale.FIT,
        autoCenter: Phaser.Scale.AUTO,
        width: 500,
        height: 500
      },
      scene: [MainScene]
  }
  
  var game = new Phaser.Game(config)
  
  