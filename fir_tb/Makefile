COURSE  = /clear/www/htdocs/comp321

CC      = gcc
CFLAGS  = -std=c99 -Wall -g
LDLIBS  = -lnsl -lpthread -lrt

PROG    = fir_tb
OBJS    = fir_tb.o fir.o

all: ${PROG}

${PROG}: ${OBJS}
	${CC} ${CFLAGS} -o ${PROG} ${OBJS} ${LDLIBS}

fir.o: fir.c fir.h
	${CC} ${CFLAGS} -I/include -c $< 

fir_tb.o: fir_tb.c fir.h
	${CC} ${CFLAGS} -I/include -c $< 

clean:
	${RM} *.o ${PROG} core.[1-9]*

.PHONY: clean
