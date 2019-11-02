

const CELL_SIZE = 15; // px
const NULL_COLOR  = "#CCCCCC";
const HEAD_COLOR  = "#0000FF";
const TAIL_COLOR  = "#00CCFF";
const CANDY_COLOR = "#FF0000";




const width = 35;
const length = 35;


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

	ctx.stroke();
};







drawCells();



