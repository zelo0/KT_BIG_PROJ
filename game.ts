import Phaser from 'phaser'
let space
function preload(){
    this.load.image('background','UIUX/background/background.jpg')
    this.load.image('front','UIUX/character/back.png')
    this.load.image('back','UIUX/character/front.png')
    this.load.spritesheet('chr','UIUX/character/chr_sprite.png',{
        frameWidth:150,
        frameHeight:158,
    }) //300*158 > 0*0 150*158 
    
}
function create(){
    this.add.image(400,300,'background')
    //this.add.image(250,350,'chr','__BASE').setOrigin(0)

    this.anims.create({
        key:'move',
        frames: this.anims.generateFrameNumbers('chr',{}),
        frameRate: 2,
        yoyo:false,
        repeat:-1,
    })

    this.sprite = this.add.sprite(250,350,'chr')
    this.sprite.anims.load('move')
    space = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE)

}

function update(){
    // this.sprite.anims.play('move')
    // this.sprite.anims.play('move')
    if(Phaser.Input.Keyboard.JustDown(space)){
        this.sprite.anims.load('move')
        this.sprite.anims.play('move')
    }
}


const config = {
    type: Phaser.AUTO,
    width: 800,
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