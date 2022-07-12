testText = ['Given$a$text$file$of$many$lines',
            'where$fields$within$a$line$',
            'are$delineated$by$a$single$"dollar"$character',
            'write$a$program',
            'that$aligns$each$column$of$fields',
            'by$ensuring$that$words$in$each$',
            'column$are$separated$by$at$least$one$space.',
            'Further,$allow$for$each$word$in$a$column$to$be$either$left$',
            'justified,$right$justified',
            'or$center$justified$within$its$column.']


def format_text(inputs, justification):

    output_text = ''
    column_size = 0
    for line in inputs:
        text = line.split('$')

        for word in text:
            if len(word) > column_size:
                column_size = len(word)

    for line in inputs:
        line_just = ''
        text = line.split('$')

        for word in text:
            if justification == 'right':
                line_just += word.rjust(column_size) + ' '
            if justification == 'left':
                line_just += word.ljust(column_size) + ' '
            if justification == 'center':
                line_just += word.center(column_size) + ' '
            if word == text[-1]:
                line_just += '\n'

        output_text += line_just

    return output_text


print(format_text(testText, 'left'))
