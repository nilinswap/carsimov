

const CELL_SIZE = 15; // px
const NULL_COLOR  = "#FFFFFF";
const BLOCK_COLOR  = "#0000FF";
const CAR_COLOR  = "#00CCFF";


function makeStruct(names) {
  var names = names.split(' ');
  var count = names.length;
  function constructor() {
    for (var i = 0; i < count; i++) {
      this[names[i]] = arguments[i];
    }
  }
  return constructor;
}

//typedeffing two structures a block is defined by diagonal corners each corner of cordinates cord
var Block = makeStruct("lt rb");
var Cord = makeStruct("x y");



//map is a list of blocks and everything between blocks are roads
var map = [];

let map_result = null;
let car_pos = new Cord(0, 0);
$(function() {
    $.ajax({
        url: '/api/random_map',
        success: function(data) {
            map_result = JSON.parse(data)
            console.log("map", map )
            map = []
            for (b of map_result.block_list){
                lt = new Cord(b.lt.x, b.lt.y);
                rb = new Cord(b.rb.x, b.rb.y);
                block = new Block(lt, rb);
                map.push(block)
            }
            car_pos = new Cord(map_result.car_pos.x, map_result.car_pos.y);;
            console.log("map 3", map )
            //$('#from_python').html("hi " + data['name'] + ", this is Javeh. (sent by python)");
        }
    });

})

console.log("map", map)

const width = 20;
const length = 20;


const canvas = document.getElementById("map-canvas");
canvas.height = (CELL_SIZE + 1) * length + 1;
canvas.width = (CELL_SIZE + 1) * width + 1;

const ctx = canvas.getContext('2d');


const drawCells = () => {


	ctx.beginPath();


	//draw raw cells
	for (let row = 0; row < length; row++){
		for (let col = 0; col < width; col++){
            ctx.fillStyle = NULL_COLOR;
			ctx.fillRect(
				col * (CELL_SIZE + 1) + 1,
				row * (CELL_SIZE + 1) + 1,
				CELL_SIZE,
				CELL_SIZE
			);
		}
	}

    //draw blocks
	for (block of map){
        for (let row = block.lt.x; row <= block.rb.x; row++){
            for (let col = block.lt.y; col <= block.rb.y; col++){
                ctx.fillStyle = BLOCK_COLOR;
                ctx.fillRect(
                    col * (CELL_SIZE + 1) + 1,
                    row * (CELL_SIZE + 1) + 1,
                    CELL_SIZE,
                    CELL_SIZE
                );
            }
        }
	}

	//draw car
	ctx.fillStyle = CAR_COLOR;
	ctx.fillRect(
                    col * (CELL_SIZE + 1) + 1,
                    row * (CELL_SIZE + 1) + 1,
                    CELL_SIZE,
                    CELL_SIZE
                );


	ctx.stroke();
};
setTimeout(
drawCells
 , 3000);









