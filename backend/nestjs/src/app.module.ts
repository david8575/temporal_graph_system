import { Module } from '@nestjs/common';
import { GraphController } from './graph/graph.controller';
import { GraphService } from './graph/graph.service';

@Module({
  controllers: [GraphController],
  providers: [GraphService],
})
export class AppModule {}
