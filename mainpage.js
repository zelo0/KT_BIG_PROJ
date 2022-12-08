import Phaser from 'phaser'
function preload(){
  this.load.image('start', 'UIUX/ui/게임시작.png')
  this.load.image('dic', 'UIUX/ui/백과사전.png')
  this.load.image('analysis', 'UIUX/ui/분석.png')
  this.load.image('store', 'UIUX/ui/상점.png')
  this.load.image('setting', 'UIUX/ui/설정.png')
  this.load.image('skills', 'UIUX/ui/스킬.png')
  this.load.image('acievement', 'UIUX/ui/업적.png')
  this.load.image('namespace', 'UIUX/ui/namespace.png')
  this.load.image('status', 'UIUX/ui/status.png')
  this.load.image('background', 'UIUX/ui/background.jpg')
}

function create(){
  this.add.image(150,300,'background')
  var setting = this.add.image(270,30,'setting').setScale(0.3).setInteractive({cursor:'pointer'})
  this.add.image(150,30,'namespace').setScale(0.3)
  var status = this.add.image(150,130,'status').setScale(0.3).setInteractive({cursor:'pointer'})
  this.add.image(60,220,'dic').setScale(0.3).setInteractive({cursor:'pointer'})
  this.add.image(60,270,'acievement').setScale(0.3).setInteractive({cursor:'pointer'})
  this.add.image(240,530,'start').setScale(0.3).setInteractive({cursor:'pointer'})
  this.add.image(255,440,'store').setScale(0.3).setInteractive({cursor:'pointer'})
  this.add.image(175,465,'skills').setScale(0.3).setInteractive({cursor:'pointer'})
  this.add.image(145,545,'analysis').setScale(0.3).setInteractive({cursor:'pointer'})

  status.on('pointerover', function(event){
    this.setTint(0x50bcdf)
  })
  status.on('pointerout', function(event){
    this.clearTint()
  })

  setting.on('pointerover', function(event){
    this.setTint(0x50bcdf)
  })
  setting.on('pointerout', function(event){
    this.clearTint()
  })

  //요소들을 하나로 묶어보자
}

function update(){
  
}

const config = {
  type: Phaser.AUTO,
  width: 300,
  height: 600,
  physics: {
      default: 'arcade',
      arcade: {
          debug: false,
          gravity: {
              y: 0
          }
      }
  },
  backgroundColor: '#2d2d2d',
  scene: {
    preload: preload,
    create: create,
    update:update,
  },
  scale: {
      mode: Phaser.Scale.ScaleModes.FIT
  }
}
var game =  new Phaser.Game(config)