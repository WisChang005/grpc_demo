package protobuf

import (
	"context"
	"fmt"
)


type Server struct{}


func (s *Server) SayHello(ctx context.Context, in *HelloRequest) (*HelloResponse, error) {
	fmt.Println("Receive message: ", in.Name)
	return &HelloResponse{Message: "Hello " + in.Name}, nil
}



func (s *Server) mustEmbedUnimplementedTesterServer() {}
