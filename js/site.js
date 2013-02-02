
var debug, stageWidth, stageHeight, docHeight = null;

$('document').ready(init);
//$(window).load(init);

function init(){    

	
	//$('body').html('Funcionando!');
	
    /* Stats */
    if(debug){

        if(Modernizr.canvas){

            Modernizr.load({
                load: 'js/Stats.js',
                complete: function () {
                    
                    var stats = new Stats();
                    stats.setMode(0);

                    $('html').append(stats.domElement);
                    setInterval(function(){
                        stats.begin();  
                        stats.end();    
                    }, 1000 / 60 );

                }
            });

        }

    }

}




function _resize(){

	stageWidth = $(window).width();
	stageHeight = $(window).height();
	docHeight = $(document).height();

}

function resizeImgBg(img){
    
    $(img).attr('height', '');
    $(img).attr('width', stageWidth - 14);
    
    if($(img).height() < stageHeight){      
        $(img).attr('height', stageHeight);
        $(img).attr('width', '');
    }

}
