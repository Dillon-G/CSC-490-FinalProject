(function () {
    var Message;    
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                var $message;
                $message = $($('.message_template').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
        return this;
    };

    //Chatbox functionality
    $(function () {
        //Setting up the text box functionality
        var getMessageText, message_side, sendMessage;
        message_side = 'left';      //Controls where messages start, left means right, right means left.
        getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };
    
        //Controls how messages appear
        sendMessage = function (text) {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = message_side === 'left' ? 'right' : 'left';
            
            //Converts the user unput text into a message which is then printed
            message = new Message({
                text: text,
                message_side: message_side
            });
            message.draw(); //Prints the message in the text box
            
            //Scrolls the text box, currently wrong
            return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        };
       
       //Sends text with button
        $('.send_message').click(function (e) {
            return sendMessage(getMessageText());
        });
       
       //Sends text with enter key
        $('.message_input').keyup(function (e) {
            if (e.which === 13) {
                return sendMessage(getMessageText());
            }
        });
    });
}.call(this)); 